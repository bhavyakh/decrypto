class A1Z26:
    # Protected:
    def _A1Z26_decrypt(cistring):

        string = ""
        # Split string at " "
        data = cistring.split()

        for char in data:
            if(ord(char) > ord('z')):
                raise ValueError("Larger than 26")
                break
            char = chr(int(char) + 96)  # Convert number to letter
            string += char
        return(string)

    # Public:
    @classmethod
    def decrypt(cls, message, key=None):
        """Decrypts A1Z26 Cypher :  
        A corresponds to 1, B to 2 ... Z to 26
        More at:
        https://www.dcode.fr/letter-number-cipher

        Args:
            message (str): encrypted text

        Returns:
            dict: {"A1Z26" : [output]}
        """
        # Decrypt string by converting each number to a letter
        try:
            output = cls._A1Z26_decrypt(message)
        except:
            output = "N/A"
        return({"A1Z26": output})      # Return cipher dictionary
