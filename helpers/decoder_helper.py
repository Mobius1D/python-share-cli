
def decoder_helper(decryptor, d_filename):
    # given a filename and an decryptor this function encrypts the file and returns the decrypted file object
    # decryptor is the decryption function that implements the algo
    # d_filename is the decryptor filename
    decrypted_data = None

    with open(d_filename, "rb") as file:
        file_data = file.read()
        decrypted_data = decryptor(file_data)
    

    # the decrypted data can be used to send the file
    return decrypted_data

