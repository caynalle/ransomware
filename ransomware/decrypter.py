from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted)

def decrypt_all_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key)

if __name__ == "__main__":
    # Load the key from the key file
    with open("key.key", "rb") as key_file:
        key = key_file.read()

    # Specify the directory where encrypted files are located
    encrypted_directory = os.path.join(os.path.expanduser("~"), "C:\\Users\\User\\Desktop")

    # Decrypt all files in the specified directory
    decrypt_all_files(encrypted_directory, key)
