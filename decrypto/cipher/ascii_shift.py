class AsciiShift:

    def _decrypt(message, key=None):
        ans = ""
        # traverse message
        for i in range(len(message)):
            char = message[i]
            ans += chr((ord(char) + key) % 255)

        return ans

    @classmethod
    def decrypt(cls, message):
        data = {}
        # traverse
        for i in range(1, 255):
            data.update({i: cls._decrypt(message, key=i)})
        return {"ASCII-shift": data}
