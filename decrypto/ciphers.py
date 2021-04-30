from decrypto.cipher.detectEnglish import isEnglish
import json
from decrypto.cipher.list import cipherList
from json2html import *


class Cipher():

    def __init__(self, message, category, key=None):
        self.message = message
        self.key = key
        self.category = category
        self.final = {}
        # List of all ciphers functions
        self.list = cipherList
        # TODO: Bacon, keyboard

    def decrypt(self, message, key):
        # Categories of defined ciphers
        _category = ['alpha_nonkeyed', 'alphanumeric-nonkeyed',
                     'numeric-nonkeyed', 'alpha_keyed', 'alpha_keyed_unknown']
        input_key = key
        data = {}
        for key, value in self.list[_category[self.category]].items():
            print(input_key)
            if not isinstance(value, dict):
                if(input_key == ''):
                    data.update({key: value(self.message)})
                else:
                    data.update({key: value(self.message, input_key)})

        self._toenglish(data, carrier="")
        print(self.final)
        data.update({"english": self.final})
        self.final = None
        # e = json2html.convert(json=json.dumps(data))
        e = json.dumps(data)
        return e

    # Checks if the solved cipher is an english sentence for better results

    def _toenglish(self, data, carrier=""):
        for key, value in data.items():

            if isinstance(value, dict):
                self._toenglish(value, key)
            else:
                if isEnglish(value, wordPercentage=40):
                    self.final.update({(str(carrier) + " " + str(key)): value})
