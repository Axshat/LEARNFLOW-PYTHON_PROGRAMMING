from cryptography.fernet import Fernet
import json
import os
import random
import string

# Path to store the encrypted passwords
PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Function to load the key from the file
def load_key():
    return open(KEY_FILE, "rb").read()

# Function to encrypt a password
def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to load passwords from the file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save passwords to the file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Main function to run the password manager
def password_manager():
    if not os.path.exists(KEY_FILE):
        generate_key()
    key = load_key()

    passwords = load_passwords()

    while True:
        print("Password Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a strong password")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            category = input("Enter the category: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            if category not in passwords:
                passwords[category] = []

            encrypted_password = encrypt_password(password, key)
            passwords[category].append({"username": username, "password": encrypted_password})
            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == '2':
            category = input("Enter the category: ")

            if category in passwords:
                for entry in passwords[category]:
                    decrypted_password = decrypt_password(entry["password"], key)
                    print(f"Username: {entry['username']}, Password: {decrypted_password}")
            else:
                print("No passwords found for this category.")

        elif choice == '3':
            length = int(input("Enter the desired length of the password: "))
            strong_password = generate_strong_password(length)
            print(f"Generated strong password: {strong_password}")

        elif choice == '4':
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    password_manager()
