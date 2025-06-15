import os
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from hashlib import sha256

def generate_key(password: str) -> bytes:
    hashed = sha256(password.encode()).digest()
    return urlsafe_b64encode(hashed)

def get_fernet(password: str) -> Fernet:
    return Fernet(generate_key(password))

def encrypt_file(filepath: str, password: str):
    if not os.path.isfile(filepath):
        print(f"❌ File '{filepath}' does not exist.")
        return

    fernet = get_fernet(password)

    with open(filepath, 'rb') as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)
    encrypted_file_path = filepath + '.enc'

    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)

    print(f"✅ Encrypted file saved as: {encrypted_file_path}")

def decrypt_file(filepath: str, password: str):
    if not os.path.isfile(filepath):
        print(f"❌ File '{filepath}' does not exist.")
        return

    if not filepath.endswith('.enc'):
        print("❌ The file does not appear to be an encrypted (.enc) file.")
        return

    fernet = get_fernet(password)

    with open(filepath, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        print("❌ Decryption failed. Incorrect password or file is corrupted.")
        return

    output_path = filepath[:-4] + '.dec'

    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)

    print(f"✅ Decrypted file saved as: {output_path}")
