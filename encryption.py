import pyAesCrypt
import os

import pyAesCrypt
import os

# Encryption function
def encryption(file, password):
    # Set buffer size
    buffer_size = 512 * 1024

    # Call encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",  # Add ".crp" extension
        password,
        buffer_size
    )

    # Display a message indicating the file is encrypted
    print(f"[File '{str(file)}' has been encrypted]")

    # Remove the original file
    os.remove(file)

# Directory scanning function
def encrypt_by_dirs(dir, password):
    # Traverse through all subdirectories and files in the specified directory
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            # If a file is found, encrypt it
            try:
                encryption(file_path, password)
            except Exception as ex:
                print(f"Error encrypting file {file_path}: {ex}")

# Input password
password = input("Enter the password for encryption: ")
directory_path = r"C:\Users\scala\Desktop\secret"  # Specify the directory path
encrypt_by_dirs(directory_path, password)
