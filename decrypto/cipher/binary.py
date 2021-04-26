import binascii


class Binary:

    @classmethod
    def decrypt(cls, message, key=None):
        """Converts from Binary to ASCII
        Uses binascii library
        More at:
        https://en.wikipedia.org/wiki/Binary_number

        Args:
            message (str): encryted text

        Returns:
            dict: {"Binary" : [output]}
        """
        output = ""
        # Whitespaces are irrelevant
        message = message.replace(" ", "")
        try:
            n = int(message, 2)
            output = binascii.unhexlify('%x' % n).decode("utf-8")
        except:
            output = "N/A"
        return {"Binary ": output}
