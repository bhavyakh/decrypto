from decrypto.cipher import (
    Atbash, Rot, RailFence, Basen, AsciiShift, Binary, T9Text, DTMF, Periodic, Prime, A1Z26, Vigenere, VigenereBreaker)
from decrypto.cipher.detectEnglish import isEnglish
import json

from json2html import *


class Cipher():

    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        self.category = 1

        # List of all ciphers functions
        self.list = {
            "alpha_nonkeyed": {
                "AtBash": Atbash.decrypt,
                "Rot - n": Rot.decrypt,
                "Railfence": RailFence.decrypt
            },
            "alphanumeric-nonkeyed": {
                "Base - n": Basen.decrypt,
                "Ascii shift": AsciiShift.decrypt
            },
            "numeric-nonkeyed": {
                "T9Numbers": T9Text.decrypt,
                "DTMF": DTMF.decrypt,
                "Binary": Binary.decrypt,
                "Periodic Elements to text": Periodic.decrypt,
                "Prime indexing": Prime.decrypt,
                "A1Z26": A1Z26.decrypt
            },
            "alpha_keyed": {
                "Viginere": Vigenere.decrypt
            },
            "alpha_keyed_unknown": {
                "Viginere Breaker": VigenereBreaker.decrypt
            }
        }
        # TODO: Bacon, keyboard

    def decrypt(self, message, key):
        # Categories of defined ciphers
        _category = ['alpha_nonkeyed', 'alphanumeric-nonkeyed',
                     'numeric-nonkeyed', 'alpha_keyed', 'alpha_keyed_unknown']

        data = {}
        for key, value in self.list[_category[1]].items():

            if not isinstance(value, dict):
                data.update(value(self.message))

        data.update({"english": self._toenglish(data, carrier="")})
        e = json2html.convert(json=json.dumps(data))

        return e

    # Checks if the solved cipher is an english sentence for better results

    def _toenglish(self, data, carrier=""):
        final = {}
        for key, value in data.items():
            if isinstance(value, dict):
                self._toenglish(value, key)
            else:
                if isEnglish(value, wordPercentage=25):
                    final.update({str(carrier) + " " + key: value})

        return final
