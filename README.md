# 🔐 Secure File Encryption/Decryption Tool (CLI)

This is a Python-based command-line tool that securely encrypts and decrypts files using AES encryption through the `cryptography` module.

## 🔧 Features
- File encryption & decryption using Fernet (AES)
- Password-based key generation using SHA-256
- CLI interface with `argparse`
- Easy to use and lightweight

## 🚀 Usage

# Encrypt a file
python main.py --encrypt yourfile.txt --password yourPassword123

# Decrypt a file
python main.py --decrypt yourfile.txt.enc --password yourPassword123

