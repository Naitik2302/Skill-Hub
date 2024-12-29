from flask import Flask, request, jsonify
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

def add_padding(data):
    padding_length = 16 - len(data) % 16
    return data + (chr(padding_length) * padding_length)

def remove_padding(data):
    return data[:-ord(data[-1])]

def create_key(length=16):
    if length not in [16, 24, 32]:
        raise ValueError("Key length must be either 16, 24, or 32 bytes.")
    return get_random_bytes(length)

def encrypt_data(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_data = add_padding(plaintext).encode('utf-8')
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_data(ciphertext, key):
    decoded = base64.b64decode(ciphertext)
    iv = decoded[:16]
    actual_data = decoded[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(actual_data)
    return remove_padding(decrypted.decode('utf-8'))

@app.route('/generate-key', methods=['GET'])
def generate_key():
    try:
        key = create_key()
        return jsonify({"key": base64.b64encode(key).decode('utf-8')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        key = base64.b64decode(data.get("key", ""))
        plaintext = data.get("text", "")

        if not plaintext or not key:
            return jsonify({"error": "Both 'key' and 'text' are required."}), 400

        encrypted_text = encrypt_data(plaintext, key)
        return jsonify({"encrypted_text": encrypted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        key = base64.b64decode(data.get("key", ""))
        ciphertext = data.get("text", "")

        if not ciphertext or not key:
            return jsonify({"error": "Both 'key' and 'text' are required."}), 400

        decrypted_text = decrypt_data(ciphertext, key)
        return jsonify({"decrypted_text": decrypted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)