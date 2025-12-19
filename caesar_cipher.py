
# Caesar Cipher

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text (str): The input text to be processed.
        shift (int): The number of positions to shift the letters.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The processed text.
    """

    result = ""

    for char in text:
        if char.isalpha():   # Process only alphabetic characters
            start = ord('a') if char.islower() else ord('A')

            if mode == 'encrypt':
                shifted_char_code = (ord(char) - start + shift) % 26 + start

            elif mode == 'decrypt':
                shifted_char_code = (ord(char) - start - shift) % 26 + start

            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")

            result += (shifted_char_code)
        else:
            result += char  # Keep non-alphabetic characters as they are

    return result


def encrpt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - start + shift) % 26 + start
            print(shifted)
            encrypted += chr(shifted)
        else:
            encrypted += char

    return encrypted


def dencrpt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - start - shift) % 26 + start
            decrypted += chr(shifted)
        else:
            decrypted += char

    return decrypted


# Example Usage:
# message = "Hello, World!"
# key = 3

# Encryption
# encrypted_message = caesar_cipher(message, key, "encrypt")
# print("Original:", message)
# print("Encrypted:", encrypted_message)

# # Decryption
# decrypted_message = caesar_cipher(encrypted_message, key, "decrypt")
# print("Decrypted:", decrypted_message)
# chr
message1 = "hiiii"
key= 3

user_input = input("Enter the message: ")
user_inputkey = int(input("Enter the key : "))

if 1 < user_inputkey < 25:
   final_encrpted =  encrpt(user_input, user_inputkey)
   print(final_encrpted)
   print("the decrpted key is: "+dencrpt(final_encrpted,user_inputkey))

else:
    print("Wrong key!")
    







