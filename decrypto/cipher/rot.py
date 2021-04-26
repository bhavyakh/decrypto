class Rot:

    def _decrypt(message, key=None):
        ans = ""
        key = 26 - key
        # traverse message
        for i in range(len(message)):
            char = message[i]
            if char.isalpha():
                ans += chr((ord(char) + key - 97) % 26 + 97)
            else:
                ans += char

        return ans

    @classmethod
    def decrypt(cls, message):
        """Decrypts ROT-N Cypher :  
        Each letter in the string is moved by N charcters
        More at:
        https://en.wikipedia.org/wiki/ROT13

        Args:
            message (str): encrypted text

        Returns:
            dict: {"ROT" : { 1,2...26 : [output]}}
        """
        message = message.lower()
        data = {}
        # traverse message
        for i in range(1, 26):
            data.update({i: cls._decrypt(message, key=i)})
        return {"Rot": data}
