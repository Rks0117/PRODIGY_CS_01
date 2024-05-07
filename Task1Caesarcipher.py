def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            ascii_val = ord(char)  # Get the ASCII value of the character
            shifted_val = ascii_val + shift  # Shift the ASCII value by the shift amount
            if char.islower():  # Check if the character is lowercase
                if shifted_val > ord('z'):  # Check if the shifted value exceeds 'z'
                    shifted_val -= 26  # Wrap around to 'a' if exceeded
            elif char.isupper():  # Check if the character is uppercase
                if shifted_val > ord('Z'):  # Check if the shifted value exceeds 'Z'
                    shifted_val -= 26  # Wrap around to 'A' if exceeded
            encrypted_text += chr(shifted_val)  # Convert the shifted ASCII value back to a character and add to the encrypted text
        else:
            encrypted_text += char  # Add non-alphabetic characters as is
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            ascii_val = ord(char)  # Get the ASCII value of the character
            shifted_val = ascii_val - shift  # Shift the ASCII value back by the shift amount
            if char.islower():  # Check if the character is lowercase
                if shifted_val < ord('a'):  # Check if the shifted value is less than 'a'
                    shifted_val += 26  # Wrap around to 'z' if less than 'a'
            elif char.isupper():  # Check if the character is uppercase
                if shifted_val < ord('A'):  # Check if the shifted value is less than 'A'
                    shifted_val += 26  # Wrap around to 'Z' if less than 'A'
            decrypted_text += chr(shifted_val)  # Convert the shifted ASCII value back to a character and add to the decrypted text
        else:
            decrypted_text += char  # Add non-alphabetic characters as is
    return decrypted_text

while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        message = input("Enter a message to encrypt: ")
        shift = int(input("Enter the shift value for encryption: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == '2':
        message = input("Enter a message to decrypt: ")
        shift = int(input("Enter the shift value for decryption: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")