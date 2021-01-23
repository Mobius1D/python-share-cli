def encoder_helper(encryptor, s_filename):
    # given a filename and an encryptor this function encrypts the file and returns the encrypted file object
    # encryptor is the encryption function that implements the algo
    # s_filename is the source filename
    encrypted_data = None

    with open(s_filename, "rb") as file:
        file_data = file.read()
        encrypted_data = encryptor(file_data)
    

    # the encrypted data can be used to send the file
    return encrypted_data


