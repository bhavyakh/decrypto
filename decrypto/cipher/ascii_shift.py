class AsciiShift:
    # Protected:
    def _decrypt(message, key=None):
        ans = ""
        # traverse message
        for i in range(len(message)):
            char = message[i]
            # Adds key -> % 255
            ans += chr((ord(char) + key) % 255)

        return ans

    # Public:
    @classmethod
    def decrypt(cls, message, key=None):
        """Decrypts ASCII Shift
        Each charecter can be shifted be k ascii characters
        from 1 to 255
        More at:
        https://www.dcode.fr/ascii-shift-cipher
        Args:
            message (str): encrypted text

        Returns:
            dict: {nested dict with the output}
        """
        output = {}
        # traverse
        for i in range(1, 255):
            output.update({i: cls._decrypt(message, key=i)})
        return {"ASCII-shift": output}
