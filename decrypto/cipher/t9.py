class T9Text:

    def _to_char(strokes):
        _keys = {
            '2': "abc", '3': "def",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz",
            '0': " "
        }
        return _keys[strokes[0]][len(strokes) - 1]

    @classmethod
    def _make_text(cls, keypad_strokes):
        text = ""
        for i in keypad_strokes.split():
            char = cls._to_char(i)
            if char:
                text += char

        return text

    @classmethod
    def decrypt(cls, message):
        """Decrypts T9 Cypher :  
        Each numeral corresponds to letters as in 
        T9 keypad
        More at:
        https://en.wikipedia.org/wiki/T9_(predictive_text)

        Args:
            message (str): encrypted text

        Returns:
            dict: {"T9" : [output]}
        """
        try:
            t9 = cls._make_text(message)
        except:
            t9 = "N/A"
        return {"T9": t9}
