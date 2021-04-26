class DTMF:

    @classmethod
    def _dtmf(cls, keypad_strokes):
        text = ""
        _keys = {"1336-941": "0",
                 "1209-697": "1",
                 "1336-697": "2",
                 "1477-697": "3",
                 "1209-770": "4",
                 "1336-770": "5",
                 "1477-770": "6",
                 "1209-852": "7",
                 "1336-852": "8",
                 "1477-852": "9"
                 }
        for i in keypad_strokes.split():
            text += (_keys[i])
        return text

    @classmethod
    def decrypt(cls, message):
        """Decrypts DTMF Cypher :  
        Each numeral string represents a number
        as given in _keys
        More at:
        https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling

        Args:
            message (str): encrypted text

        Returns:
            dict: {"DTMF" : [output]}
        """
        try:
            dtmf = cls._dtmf(message)
        except:
            dtmf = "N/A"
        return {"DTMF": dtmf}
