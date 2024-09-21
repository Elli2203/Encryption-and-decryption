import pyAesCrypt
import os

# Decryption function
def decryption(file, password):
    # Set buffer size
    buffer_size = 512 * 1024

    # Call decryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),  # Remove ".crp" extension
        password,
        buffer_size
    )

    # Display a message indicating the file is decrypted
    print(f"[File '{str(os.path.splitext(file)[0])}' has been decrypted]")

    # Remove the encrypted file
    os.remove(file)

# Directory scanning function
def decrypt_by_dirs(dir, password):
    # Traverse through all subdirectories and files in the specified directory
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            # If a file with ".crp" extension is found, decrypt it
            if file.endswith('.crp'):
                try:
                    decryption(file_path, password)
                except Exception as ex:
                    print(f"Error decrypting file {file_path}: {ex}")

# Input password
password = input("Enter the password for decryption: ")
directory_path = r""  # Specify the directory path
decrypt_by_dirs(directory_path, password)
