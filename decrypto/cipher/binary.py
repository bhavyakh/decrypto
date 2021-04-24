import binascii


class Binary:

    @classmethod
    def decrypt(cls, message, key=None):
        ans = ""
        message = message.replace(" ", "")
        try:
            n = int(message, 2)
            ans = binascii.unhexlify('%x' % n).decode("utf-8")
        except:
            ans = "N/A"
        return {"Binary ": ans}
