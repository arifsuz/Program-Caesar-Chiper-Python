# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to encrypt the text
def encrypt(text, shift_key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = (position + shift_key) % 52
            new_char = alphabet[new_position]
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift_key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = (position - shift_key) % 52
            new_char = alphabet[new_position]
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

# Main function to run the program
def main():
    choice = input("Do you want to encrypt or decrypt? (E/D): ")
    if choice.lower() == 'e':
        text = input("Enter the text to encrypt: ")
        shift_key = int(input("Enter the shift key: "))
        print("Encrypted text: ", encrypt(text, shift_key))
    elif choice.lower() == 'd':
        text = input("Enter the text to decrypt: ")
        shift_key = int(input("Enter the shift key: "))
        print("Decrypted text: ", decrypt(text, shift_key))
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

# Call the main function
main()
