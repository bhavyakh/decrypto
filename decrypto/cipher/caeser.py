class Caesar:

    def decrypt(message, s):
        message = message.lower()
        ans = ""
        s = 26 - s

        # traverse message
        for i in range(len(message)):
            char = message[i]
            ans += chr((ord(char) + s - 97) % 26 + 97)

        return ans
