def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            # For each character, it checks if
            # it is an alphabet letter (char.isalpha()). If it is, it calculates the shifted
            # character based on whether it's lowercase or uppercase and appends it to the ciphertext.
            shift_amount = shift % 26
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            ciphertext += shifted
        elif char.isdigit():
            shifted = str((int(char) + shift) % 10)
            ciphertext += shifted
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            plaintext += shifted
        elif char.isdigit():
            shifted = str((int(char) - shift) % 10)
            plaintext += shifted
        else:
            plaintext += char
    return plaintext

def caesar_brute_force(ciphertext):
    decrypted_texts = []
    for shift in range(26):
        decrypted_text = ''
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                else:
                    decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def get_input():
    plaintext = input("Enter the text you want to encrypt and decrypt: ")
    shift_str = input("Enter the shift (a positive number for encryption, a negative number for decryption): ")
    if shift_str.isdigit():
        shift = int(shift_str)
    else:
        print("Invalid input for shift. Please enter a valid number.")
        return None, None
    return plaintext, shift


plaintext, shift = get_input()

if plaintext is not None and shift is not None:
    encrypted_text = caesar_encrypt(plaintext, shift)
    print("Encrypted:", encrypted_text)

    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Decrypted:", decrypted_text)

    decrypted_texts = caesar_brute_force(encrypted_text)
    for i, text in enumerate(decrypted_texts):
        print(f"Shift {i}: {text}")

