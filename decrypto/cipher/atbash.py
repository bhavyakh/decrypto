class Atbash:

    @classmethod
    def decrypt(cls, message, key = None):
        message = message.lower()
        ans = ""
        alphabet = u"abcdefghijklmnopqrstuvwxyz"

        for char in message:
            alphIndex = len(alphabet) - (alphabet.index(char)) - 1
            ans += alphabet[alphIndex]
        return {"Atbash" : ans}
