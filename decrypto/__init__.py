from flask import Flask, render_template, request
from flask.helpers import get_debug_flag
from .ciphers import Cipher
from .config import DevConfig, ProdConfig
app = Flask(__name__)

# If using developement configuration
if get_debug_flag():
    app.config.from_object(DevConfig)
# Using a production configuration
else:
    app.config.from_object(ProdConfig)


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
            elif(string.isnumeric()):
                category = 2
            else:
                category = 1

    return category
