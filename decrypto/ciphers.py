from decrypto.cipher import (
    Atbash, Rot, RailFence, Basen, AsciiShift, Binary, T9Text, DTMF, Periodic, Prime, A1Z26, Vigenere, VigenereBreaker)
import json
from json2html import *


class Cipher():
    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        self.category = 1
        '''if self.key:
            self.category = 3
        else:
            self.category = 1'''
        # TODO: Bacon, keyboard

    def decrypt(self, message, key):
        if(self.category == 1):
            data = Atbash.decrypt(self.message)
            data.update(Rot.decrypt(self.message))
            data.update(RailFence.decrypt(self.message))
            data.update(Basen.decrypt(self.message))
            data.update(AsciiShift.decrypt(self.message))

            e = json2html.convert(json=json.dumps(data))
        elif(self.category == 2):
            data = T9Text.decrypt(self.message)
            data.update(DTMF.decrypt(self.message))
            data.update(Binary.decrypt(self.message))
            data.update(Periodic.decrypt(self.message))
            data.update(Prime.decrypt(self.message))
            data.update(A1Z26.decrypt(self.message))

            e = json2html.convert(json=json.dumps(data))
        elif(self.category == 3):
            data = Vigenere.decrypt(self.message, self.key)
            e = json2html.convert(json=json.dumps(data))
        elif(self.category == 4):
            data = VigenereBreaker.decrypt(self.message)
            e = json2html.convert(json=json.dumps(data))
        return e
