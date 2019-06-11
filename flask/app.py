from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
    return render_template("main.html")
@app.route("/signup/")
def main():
    return render_template("signup.html")
@app.route("/bbs/")
def main():
    return render_template("bbs.html")

if __name__ == "__main__":
    app.run()