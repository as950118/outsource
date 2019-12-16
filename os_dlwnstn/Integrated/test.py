def Generate_DigSig_On_Hashed_File(filename, privatekeyname):
    #get file
    file = open(filename, "rb")
    plaintext = file.read()
    file.close()

    #get privatekey
    file = open(privatekeyname, "rb")
    privatekey = file.read()
    file.close()

    #hasing
    myhash = SHA256.new(plaintext)  # Generate Hash
    signature = pkcs1_15.new(privatekey)  # Signature algo
    sigVal = signature.sign(myhash)  # signature value
    print("Length of Signature: ", len(sigVal))
    print("Signature: ", sigVal)
    output = sigVal + plaintext  ## concatnate message
    return output

def Generate_AES_Enc_On_DigSig_Plus_Key(file, ):
    sessionkey = Random.new().read(32)  # 256 bit
    print("Session Key: ", sessionkey)
    # encryption AES of the message
    plaintext = file.read()
    iv = Random.new().read(16)  # 128 bit
    print("IV: ", iv)
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    ciphertext = iv + obj.encrypt(plaintext)
    print("Cipher: ", ciphertext)

    # encryption RSA of the session key
    cipherrsa = PKCS1_OAEP.new(publickey)
    enc_sessionkey = cipherrsa.encrypt(sessionkey)
    print("Length of encrypted session key: ", len(enc_sessionkey))  #### Length of session key: 256 byte
    print("Encrypted Session Key:", enc_sessionkey)
    return bytes(cipherrsa), bytes(enc_sessionkey)

def B64Encoding(cipherrsa, enc_sessionkey):
    return base64.b64encode(cipherrsa), base64.b64encode(enc_sessionkey)
