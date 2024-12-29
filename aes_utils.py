from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def add_padding(data):
    padding_length = 16 - len(data) % 16
    return data + (chr(padding_length) * padding_length)

def remove_padding(data):
    return data[:-ord(data[-1])]

def create_key(length=16):
    if length not in [16, 24, 32]:
        raise ValueError("Key length must be either 16, 24, or 32 bytes.")
    return get_random_bytes(length)

def encrypt_data(plaintext, key, mode=AES.MODE_CBC):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key length must be 16, 24, or 32 bytes.")

    cipher = AES.new(key, mode)
    iv = cipher.iv
    padded_data = add_padding(plaintext).encode('utf-8')
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_data(ciphertext, key, mode=AES.MODE_CBC):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key length must be 16, 24, or 32 bytes.")

    decoded = base64.b64decode(ciphertext)
    iv = decoded[:16]
    actual_data = decoded[16:]
    cipher = AES.new(key, mode, iv)
    decrypted = cipher.decrypt(actual_data)
    return remove_padding(decrypted.decode('utf-8'))

def main():
    print("Welcome to the AES Encryption/Decryption Tool")
    print("1. Generate Random AES Key")
    print("2. Encrypt Text")
    print("3. Decrypt Text")
    choice = input("Please select an option (1/2/3): ")

    if choice == '1':
        key_size = int(input("Enter key size (16, 24, 32 bytes): "))
        key = create_key(key_size)
        print("Generated AES Key (Base64):", base64.b64encode(key).decode('utf-8'))

    elif choice == '2':
        key = base64.b64decode(input("Enter your AES key (Base64): "))
        plaintext = input("Enter text to encrypt: ")
        try:
            encrypted_text = encrypt_data(plaintext, key)
            print("Encrypted Text (Base64):", encrypted_text)
        except Exception as e:
            print("Encryption failed:", e)

    elif choice == '3':
        key = base64.b64decode(input("Enter your AES key (Base64): "))
        ciphertext = input("Enter text to decrypt (Base64): ")
        try:
            decrypted_text = decrypt_data(ciphertext, key)
            print("Decrypted Text:", decrypted_text)
        except Exception as e:
            print("Decryption failed:", e)

    else:
        print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
