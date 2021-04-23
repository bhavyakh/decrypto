from decrypto.cipher import (Atbash, Caesar, RailFence)
import json
from json2html import *

class Cipher():
    def __init__(self, message, key=None):
        self.message = message
        self.key = key

    def decrypt(self, category=1):
        if(category == 1):
            data = Atbash.decrypt(self.message)
            data.update(Caesar.decrypt(self.message))
            data.update(RailFence.decrypt(self.message))
            print(data)
            e = json2html.convert(json = json.dumps(data))
            return e
