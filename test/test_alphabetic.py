import unittest
import json
from decrypto.ciphers import Cipher


class TestAlphabetic(unittest.TestCase):

    # For alphabetic ciphers

    def test_alphabetic_no_whitespace_atbash(self):
        # Atbash kiltizn
        encryptedMessage = "KILTIZN"
        s = Cipher(message=encryptedMessage, category=0, key=None)
        data = s.decrypt()

        # Given output is in JSON -> dictionary
        calculatedOutput = json.loads(data)

        # English expression is matched
        expectedOutput = {"AtBash Atbash": "program"}
        self.assertDictEqual(calculatedOutput["english"], expectedOutput)

    def test_alphabetic_lower_whitespace_rot(self):
        # Rot 13 -> i am a regular computer user
        encryptedMessage = "v nz n erthyne pbzchgre hfre"

        # Create the cipher object and decrypt
        s = Cipher(message=encryptedMessage, category=0, key=None)
        data = s.decrypt()

        # Given output is in JSON -> dictionary
        calculatedOutput = json.loads(data)

        # English expression is matched
        expectedOutput = {"Rot 13": "i am a regular computer user"}
        self.assertDictEqual(calculatedOutput["english"], expectedOutput)

    def test_alphabetic_railfence(self):
        # Railfence 3 -> this is inspired by trains
        encryptedMessage = "t ii tnhsi nprdb risisseya"

        # Create the cipher object and decrypt
        s = Cipher(message=encryptedMessage, category=0, key=None)
        data = s.decrypt()

        # Given output is in JSON -> dictionary
        calculatedOutput = json.loads(data)

        # English expression is matched
        expectedOutput = {"RailFence 3": "this is inspired by trains"}
        self.assertDictEqual(calculatedOutput["english"], expectedOutput)


if __name__ == '__main__':
    unittest.main()
