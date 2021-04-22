class Atbash:

    def decrypt(message):
        message = message.lower()
        ans = ""
        alphabet = u"abcdefghijklmnopqrstuvwxyz"
        for char in message:
            alphIndex = len(alphabet) - (alphabet.index(char)) - 1
            ans += alphabet[alphIndex]
        return ans
