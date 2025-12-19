import math

import math

def col_transpose(text, key, mode):
    cols = len(key)
    
    if mode == "encrypt":
        message = text
        rows = math.ceil(len(message) / cols)

        msg_list = list(message)
        padding = rows * cols - len(msg_list)
        msg_list.extend("_" * padding)

        # build matrix row-wise
        matrix = []
        index = 0
        for _ in range(rows):
            matrix.append(msg_list[index:index + cols])
            index += cols

        # sorted key
        sorted_key = sorted(list(key))
        

        cipher = ""
        temp_key = key

        # read columns in sorted order
        for char in sorted_key:
            col_index = temp_key.index(char)
            for row in matrix:
                cipher += row[col_index]
            temp_key = temp_key.replace(char, "_", 1)

        return cipher


    elif mode == "decrypt":
        cipher = text
        rows = math.ceil(len(cipher) / cols)

        cipher_list = list(cipher)
        sorted_key = sorted(list(key))

        matrix = [[None] * cols for _ in range(rows)]
        index = 0
        temp_key = key

        # fill columns in sorted order
        for char in sorted_key:
            col_index = temp_key.index(char)
            for r in range(rows):
                matrix[r][col_index] = cipher_list[index]
                index += 1
            temp_key = temp_key.replace(char, "_", 1)

        # flatten matrix
        message = ""
        for r in range(rows):
            for c in range(cols):
                message += matrix[r][c]

        return message.rstrip("_")


    else:
        return "Invalid mode! Use 'encrypt' or 'decrypt'."




message=input("enter the message: ")
key= input("enter the key ")


ciphertext = col_transpose(message, key, "encrypt")
print("Encrypted:", ciphertext)

plaintext = col_transpose(ciphertext, key, "decrypt")
print("Decrypted:", plaintext)
