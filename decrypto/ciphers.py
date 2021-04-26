from decrypto.cipher import (
    Atbash, Rot, RailFence, Basen, AsciiShift, Binary, T9Text, DTMF, Periodic, Prime, A1Z26, Vigenere, VigenereBreaker)
import json
from json2html import *


class Cipher():

    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        self.category = 1
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
        '''if self.key:
            self.category = 3
        else:
            self.category = 1'''
        # TODO: Bacon, keyboard

    def decrypt(self, message, key):
        _category = ['alpha_nonkeyed', 'alphanumeric-nonkeyed',
                     'numeric-nonkeyed', 'alpha_keyed', 'alpha_keyed_unknown']

        """data = Atbash.decrypt(self.message)
            data.update(Rot.decrypt(self.message))
            data.update(RailFence.decrypt(self.message))
            data.update(Basen.decrypt(self.message))
            data.update(AsciiShift.decrypt(self.message))"""
        '''data = T9Text.decrypt(self.message)
            data.update(DTMF.decrypt(self.message))
            data.update(Binary.decrypt(self.message))
            data.update(Periodic.decrypt(self.message))
            data.update(Prime.decrypt(self.message))
            data.update(A1Z26.decrypt(self.message))
            e = json2html.convert(json=json.dumps(data))
            data = Vigenere.decrypt(self.message, self.key)
            e = json2html.convert(json=json.dumps(data))
            data = VigenereBreaker.decrypt(self.message)
            e = json2html.convert(json=json.dumps(data))'''
        data = {}
        for key, value in self.list[_category[0]].items():
            print(value)

            if not isinstance(value, dict):
                print(value)
                data.update(value(self.message))

        e = json2html.convert(json=json.dumps(data))

        return e
