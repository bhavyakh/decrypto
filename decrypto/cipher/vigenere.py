from decrypto.cipher.vigcep import _decryptMessage


class Vigenere:

    # Generate key matching to length of the message
    def _generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        return("" . join(key))

    @classmethod
    def decrypt(cls, message, key):
        """Decrypts Vigenere cipher
        Each letter has a different ROT N rotation based on
        the key given
        More at:
        https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

        Args:
            message (str): Encrypted text
            key (str): Key

        Returns:
            dict : {"Vigenere" : [output]}
        """
        # Uppercase is irrelevant
        message = message.lower()
        key = key.lower()

        key = cls._generateKey(message, key)
        output = _decryptMessage(key, message)

        return {"Vigenere": output}
