import sys
sys.path.append("../")
from cryptography.fernet import Fernet
from encoder_helper import *

# just for testing purposes
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# just for testing purposes
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()
# just for testing purposes
def encryptor(file_data):
    """
    Given a filename (str) and key (bytes), it encrypts the file and returns the encrypted file_data
    """
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    return encrypted_data

# for running and testing the code
if __name__ == "__main__":
    write_key()
    # print(encoder_helper(encryptor, "file.txt"))
    encrypted_data = encoder_helper(encryptor, "file.txt")
    print(encrypted_data)
    with open("encrypted_file.txt", "wb") as file:
        file.write(encrypted_data)

