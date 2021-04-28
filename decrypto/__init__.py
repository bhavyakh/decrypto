from flask import Flask, render_template, request
from .ciphers import Cipher
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html')


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    data = {"hi": "there"}
    returnedJSON = request.json
    message = returnedJSON['cipher']
    key = returnedJSON['key']
    category = (_getCategory(returnedJSON))
    s = Cipher(message, category, key)
    data = s.decrypt(cipher, key)
    # if request.method == 'GET':
    #     try:
    #         print(request)
    #     except:
    #         pass
    #     message = request.args.get('cipher')
    #     key = request.args.get('key')
    #     s = Cipher(message, key)
    #     data = s.decrypt(cipher, key)
    return data


def _getCategory(dic):
    category = 0
    # Vigenere break
    print(dic)
    if (dic['break']):
        category = 4
    else:
        # Alpha but keyed
        if(dic['key'] != ''):
            category = 3
        else:
            string = str(dic['cipher'])
            string = string.replace(' ', '')
            if(string.isalpha()):
                category = 0
            elif(string.isnumeric):
                category = 1
            else:
                category = 2

    return category
