class A1Z26:

    def _A1Z26_decrypt(cistring):

        string = ""                     # Placeholder variable
        data = cistring.split()         # Split string at " "

        for char in data:               # Loop through each character
            if(ord(char) > ord('z')):
                raise ValueError("Larger than 26")
                break
            char = chr(int(char) + 96)  # Convert number to letter
            string += char
        return(string)

    @classmethod
    def decrypt(cls, message):

        # Decrypt string by converting each number to a letter
        try:
            string = cls._A1Z26_decrypt(message)
        except:
            string = "N/A"
        return({"A1Z26": string})      # Return cipher dictionary
