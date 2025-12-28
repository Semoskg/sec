"""
Group members 
SAMUEL KUMELA      068
ADONIGHT ALEMAYEHU  047
MERONAWIT DEJENE    085
"""


def encrypt_rail_fence(text, rails):
    # Remove spaces and convert text to uppercase
    text = text.replace(" ", "").upper()

    # Create empty rails (lists) to store characters
    fence = [[] for _ in range(rails)]

    # Start at the first rail and move downward
    rail = 0
    direction = 1  # 1 = down, -1 = up

    # Place each character in zigzag order
    for ch in text:
        fence[rail].append(ch)     # Put character in current rail
        rail += direction          # Move to next rail

        # Reverse direction at top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Read rails row by row to form ciphertext
    return ''.join(''.join(r) for r in fence)


def decrypt_rail_fence(ciphertext, rails):
    # Get ciphertext length
    length = len(ciphertext)

    # Create empty matrix for rails
    fence = [[None] * length for _ in range(rails)]

    # Step 1: Mark zigzag positions with '*'
    rail = 0
    direction = 1
    for i in range(length):
        fence[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Step 2: Fill ciphertext characters row by row
    index = 0
    for r in range(rails):
        for c in range(length):
            if fence[r][c] == '*':
                fence[r][c] = ciphertext[index]
                index += 1

    # Step 3: Read characters again in zigzag order
    result = []
    rail = 0
    direction = 1
    for i in range(length):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Return decrypted plaintext
    return ''.join(result)


# Example usage
key = int(input("Enter number of rails: ")) 
text = input("Enter the text: ")

cipher = encrypt_rail_fence(text, key)
print("Encrypted:", cipher)

plain = decrypt_rail_fence(cipher, key)
print("Decrypted:", plain)
