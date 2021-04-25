from flask import Flask, render_template, request
from .ciphers import Cipher
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html')


@app.route("/submit", methods=['GET'])
def submit():
    if request.method == 'GET':
        message = request.args.get('cipher')
        key = request.args.get('key')
        s = Cipher(message, key)
        data = s.decrypt(cipher, key)
    return data


if __name__ == '__main__':
    app.run(debug=True, port=8080)
