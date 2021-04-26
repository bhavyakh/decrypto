class Atbash:

    # Public:
    @classmethod
    def decrypt(cls, message):
        """Decrypts AtBash Cipher
        Each letter = 26 - [letter index]
        More at:
        https://en.wikipedia.org/wiki/Atbash

        Args:
            message (str): encrypted text       

        Returns:
            dict: {"Atbash" : [output]}
        """
        message = message.lower()
        ans = ""
        # Placeholder
        alphabet = u"abcdefghijklmnopqrstuvwxyz"

        for char in message:
            if char.isalpha():
                alphIndex = len(alphabet) - (alphabet.index(char)) - 1
                ans += alphabet[alphIndex]
            else:
                ans += char
        return {"Atbash": ans}
