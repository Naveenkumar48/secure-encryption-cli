import argparse
from crypto_tool import encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(
        description='🔐 Secure File Encryption/Decryption Tool (CLI)'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encrypt', metavar='FILE', help='Path to file to encrypt')
    group.add_argument('--decrypt', metavar='FILE', help='Path to encrypted file (.enc)')

    parser.add_argument('--password', required=True, help='Password used for encryption/decryption')

    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.encrypt, args.password)
    elif args.decrypt:
        decrypt_file(args.decrypt, args.password)

if __name__ == '__main__':
    main()
