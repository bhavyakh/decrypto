from baseconv import (base16, base36)
import base64

# TODO Add error return capability for each Base


class Basen:

    def _decrypt_base16(txt):
        try:
            return {"Base16 (decimal)": base16.decode(txt)}
        except:
            return {"Base16": "N/A"}

    def _decrypt_base36(txt):
        try:
            return {"Base36 (decimal)": base36.decode(txt)}
        except:
            return {"Base36": "N/A"}

    def _decrypt_base64(txt):
        try:
            dat = base64.b64decode(txt)
            return {"Base64": dat.decode("utf-8")}
        except:
            return {"Base64": "N/A"}

    @classmethod
    def decrypt(cls, message, key=None):
        """Converts from Base16,36,64 to Decimal
        Uses baseconv and base64 packages
        More at:
        https://en.wikipedia.org/wiki/Base64

        Args:
            message (str): encryted text

        Returns:
            dict: {"Base-n" : [output]}
        """
        data = {}
        # Whitespaces irrelevant
        message = message.replace(" ", "")
        data.update(cls._decrypt_base16(message))
        data.update(cls._decrypt_base36(message))
        data.update(cls._decrypt_base64(message))
        return {"Base-n": data}
