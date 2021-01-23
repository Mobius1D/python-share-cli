import sys
sys.path.append("../")
from cryptography.fernet import Fernet
from decoder_helper import *


# just for testing purposes
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()
# just for testing purposes
def decryptor(file_data):
    """
    Given a filename (str) and key (bytes), it encrypts the file and returns the decrypted file_data
    """
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(file_data)
    return decrypted_data

# for running and testing the code
if __name__ == "__main__":
    decrypted_data = decoder_helper(decryptor, "encrypted_file.txt")
    print(decrypted_data)
    with open("decrypted_file.txt", "wb") as file:
        file.write(decrypted_data)