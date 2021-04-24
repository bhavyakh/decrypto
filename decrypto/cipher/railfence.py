class RailFence:

    def _decrypt(cipher, key):

        rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]

        # to find the direction
        dir_down = None
        row, col = 0, 0

        # mark the places with '*'
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker
            rail[row][col] = '*'
            col += 1

            # find the next row
            # using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                        (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):

            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key-1:
                dir_down = False

            # place the marker
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1

            # find the next row using
            # direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        return("".join(result))

    @classmethod
    def decrypt(cls, message):
        message = message.lower()
        data = {}
        # traverse message
        for i in range(2, 5):
            data.update({i: cls._decrypt(message, key=i)})
        return {"RailFence": data}
