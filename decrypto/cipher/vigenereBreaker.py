from decrypto.cipher.detectEnglish import isEnglish
from decrypto.cipher.vigcep import _decryptMessage


class VigenereBreaker:

    def _hackVigenere(ciphertext):
        fo = open('decrypto/static/dictionary.txt')
        words = fo.readlines()
        fo.close()
        data = {}
        for word in words:
            word = word.strip()  # remove the newline at the end
            decryptedText = _decryptMessage(word, ciphertext)
            if isEnglish(decryptedText, wordPercentage=40):
                data.update({str(word): decryptedText[:100]})
        if data is None:
            return "N/A"
        return data

    @ classmethod
    def decrypt(cls, message):
        # try:
        data = cls._hackVigenere(message)
        '''except:
            data = "N/A"'''
        return {"Vigenere": data}
