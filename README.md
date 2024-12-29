AES Encryption and Decryption Tool

Overview:

This project is a user-friendly AES (Advanced Encryption Standard) encryption and decryption tool. It provides a secure way to encrypt and decrypt text using a shared secret key. The tool is implemented with a modern, intuitive interface and a Flask backend to handle encryption and decryption processes.

Features

Key Generation: Generate a secure 256-bit encryption key.
Text Encryption: Encrypt any plaintext using the AES algorithm and a provided key.
Text Decryption: Decrypt ciphertext back to plaintext using the same key.
Separate Tabs: Separate sections for encryption and decryption for ease of use.
User-Friendly Interface: Modern and accessible UI with a clean design.

Technology Stack:

Frontend:

HTML5 & CSS3: For structure and styling.
JavaScript: For interactivity.
Bootstrap: For a responsive and polished design.

Backend:

Flask: Python-based lightweight backend framework for handling API requests.
PyCryptodome: Library for implementing AES encryption and decryption.

Other Tools:

Jinja2: Template engine for rendering HTML.

Installation and Usage:

Prerequisites:

Ensure you have the following installed:

Python (>=3.6)
pip (Python package manager)

Setup Steps

Clone the repository:

git clone https://github.com/your-repository/aes-tool.git
cd aes-tool

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate

Install required dependencies:

pip install -r requirements.txt

Start the Flask server:

python app.py
Open your browser and navigate to http://127.0.0.1:5000 to access the application.

How to Use:

Encryption:

Go to the Encryption tab.
Enter the plaintext you want to encrypt.
Provide a 256-bit encryption key (or use the generated key).
Click the "Encrypt" button to see the encrypted text.

Decryption:

Go to the Decryption tab.
Enter the ciphertext you want to decrypt.
Provide the same encryption key used during encryption.
Click the "Decrypt" button to retrieve the plaintext.

File Structure:

project-root/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/
│   ├── base.html
│   ├── encrypt.html
│   └── decrypt.html
├── app.py
├── requirements.txt
└── README.md

Security Notes:

Always use a secure, randomly generated key for encryption.
Do not share your encryption key publicly.
This tool is intended for educational purposes and should not be used for highly sensitive or production-grade encryption.

Future Enhancements:

Add file encryption and decryption support.
Enable users to save and manage their keys securely.
Implement advanced modes like AES-GCM for authenticated encryption.

Contribution:

Contributions are welcome! To contribute:
Fork the repository.
Create a feature branch.
Commit your changes and open a pull request.

Contact:
For queries or suggestions, please reach out to [naitikmittal84@gmail.com].

