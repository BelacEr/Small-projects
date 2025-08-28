from cryptography.fernet import Fernet

import sys


thank_you = "\nThank you for using the Cryptography-CLI-Tool created by BelacEr."
valid_number = "\nMake sure to enter a valid number."


def enter_number(prompt):
    """
    Make sure only whole numbers are entered for the menu.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(valid_number)
        except KeyboardInterrupt:
            print(thank_you)
            sys.exit()
        except EOFError:
            print(thank_you)
            sys.exit()


def generate_key():
    """
    Generates a key and save it into a file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    
    print("\nKey created!")


def load_key():
    """Load the previously generated key."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key not found. Please generate one first (option 1).")
        return None


def encrypt_message():
    """Encrypts a message."""
    key = load_key()
    if key is None:
        return
    
    message = input("Enter the message you want to encrypt: ")
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print("Encrypted message:", encrypted_message.decode())  # Convert to str to print.


def decrypt_message():
    """Decrypts an encrypted message."""
    key = load_key()
    if key is None:
        return
    
    encrypted_input = input("\nEnter the encrypted message: ").encode()  # To bytes
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_input)
    print("\nDecrypted message:", decrypted_message.decode())


def exit_cryptography():
    """
    Gracefully exit the cryptography tool.
    """
    print("\nExiting the program...")
    sys.exit()


def show_menu():
    print("""
    === CRYPTOGRAPHY-CLI-TOOL ===
1. Generate key (execute only once)
2. Encrypt message
3. Decrypt message
4. Exit
""")


def main():
     while True:
        show_menu()
        choice = enter_number("Enter your choice: ")

        if choice == 1:
            generate_key()
        elif choice == 2:
            encrypt_message()
        elif choice == 3:
            decrypt_message()
        elif choice == 4:
            exit_cryptography()
        else:
            print(valid_number)