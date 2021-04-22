from decrypto.cipher import (Atbash, Caesar)
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html')


@app.route("/submit", methods=['GET'])
def submit():
    if request.method == 'GET':
        message = request.args.get('cipher')
        data = "Atbash: " + \
            Atbash.decrypt(message)
        for i in range(1, 25):
            data += "Caeser: " + Caesar.decrypt(message, i) + "<br>"
    return (data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
