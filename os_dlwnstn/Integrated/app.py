# -- coding: utf-8 --
import flask
import os
import binascii
import json
from flask import request, jsonify, render_template
from werkzeug import secure_filename
from flask_socketio import SocketIO, emit
from Crypto.PublicKey import RSA
from PGP_All_Common import *



app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=['GET'])
def upload():
    # generate sender key
    sender_id = str(int(binascii.hexlify(os.urandom(24)), 24))
    sender_key = RSA.generate(2048)
    sender_privatekey = sender_key.exportKey("PEM")
    sender_publickey = sender_key.publickey().exportKey("PEM")

    sender_privatekeyname = "./sender/privatekey_{0}".format(sender_id)
    f = open(sender_privatekeyname, "wb")
    f.write(sender_privatekey)
    f.close()

    sender_publickeyname = "./sender/publickey_{0}".format(sender_id)
    f = open(sender_publickeyname, "wb")
    f.write(sender_publickey)
    f.close()

    return render_template("upload.html", sender_id = sender_id, sender_privatekey = sender_privatekey, sender_publickey = sender_publickey)

@app.route("/result", methods=['POST'])
def result():
    # Get sender info
    sender_id = request.form["sender_id"][:-1]
    sender_privatekeyname = "./sender/privatekey_{0}".format(sender_id)
    sender_publickeyname = "./sender/publickey_{0}".format(sender_id)

    # Save sender file
    sender_file = request.files["file"]
    sender_filename = "./sender/file_{0}".format(secure_filename(sender_file.filename))
    sender_file.save(sender_filename)
    mimetype = sender_file.content_type


    # Generate receiver key
    receiver_id = str(int(binascii.hexlify(os.urandom(24)), 24))
    receiver_key = RSA.generate(2048)
    receiver_privatekey = receiver_key.exportKey("PEM")
    receiver_publickey = receiver_key.publickey().exportKey("PEM")

    receiver_privatekeyname = "./receiver/privatekey_{0}".format(receiver_id)
    f = open(receiver_privatekeyname, "wb")
    f.write(receiver_privatekey)
    f.close()

    receiver_publickeyname = "./sender/publickey_{0}".format(receiver_id)
    f = open(receiver_publickeyname, "wb")
    f.write(receiver_publickey)
    f.close()


    # Hashing
    sender_hashedfilename = "./sender/hashed_{0}".format(sender_id)
    Generate_DigSig_On_Hashed_File(sender_filename, sender_privatekeyname, sender_hashedfilename)

    sender_outputname = "./sender/output_{0}".format(sender_id)
    Generate_AES_Enc_On_DigSig_Plus_Key(sender_hashedfilename, receiver_publickeyname, sender_outputname)

    sender_outputb64name = "./sender/outputb64_{0}".format(sender_id)
    B64Encoding(sender_outputname, sender_outputb64name)

    # Verify
    receiver_outputname = "./receiver/output_{0}".format(receiver_id)
    B64Decoding(sender_outputb64name, receiver_outputname)
    f = open(receiver_outputname, "rb")
    received_data = f.read()
    f.close()

    receiver_hashedfilename = "./receiver/hashed_{0}".format(receiver_id)
    Generate_AES_Dec_For_DigSig_Plus_Key(sender_outputname, receiver_privatekeyname, receiver_hashedfilename)

    decrypted_data, valid = Verify_DigSig_On_Hashed_File(receiver_hashedfilename, sender_publickeyname)

    # Text decoding
    if mimetype == "text/plain":
        decrypted_data = decrypted_data.decode("cp949")

    return render_template("result.html", filename = sender_filename, valid = valid, mimetype = mimetype, received_data = received_data, decrypted_data = decrypted_data)


app.run()