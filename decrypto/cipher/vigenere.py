class Vigenere:

    def _generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return("" . join(key))

    def _decryption(encrypt_text, key):
        orig_text = []
        for i in range(len(encrypt_text)):
            x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return("" . join(orig_text))

    @classmethod
    def decrypt(cls, message, key):
        message = message.lower()
        key = key.lower()
        key = cls._generateKey(message, key)
        ans = cls._decryption(message, key)

        return {"Vigenere": ans}
