from flask import Flask, request, jsonify
#from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
# rsa_cipher = RSACipher()

# @app.route('/api/rsa/generate_keys', methods=['GET'])
# def rsa_generate_keys():
#     """
#     Generates RSA public and private keys and saves them.
#     Returns a JSON response indicating success.
#     """
#     rsa_cipher.generate_keys()
#     return jsonify({'message': 'Keys generated successfully'})

# @app.route("/api/rsa/encrypt", methods=["POST"])
# def rsa_encrypt():
#     """
#     Encrypts a message using RSA.
#     Expects 'message' and 'key_type' (public/private) in the JSON request.
#     Returns the encrypted message in hexadecimal format.
#     """
#     data = request.json
#     message = data['message']
#     key_type = data['key_type']

#     private_key, public_key = rsa_cipher.load_keys()

#     key = None
#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'}), 400 # Added status code for error

#     encrypted_message = rsa_cipher.encrypt(message, key)
#     # Convert bytes to hexadecimal string for JSON serialization
#     encrypted_hex = encrypted_message.hex()
#     return jsonify({'encrypted_message': encrypted_hex})

# @app.route("/api/rsa/decrypt", methods=["POST"])
# def rsa_decrypt():
#     """
#     Decrypts a ciphertext using RSA.
#     Expects 'ciphertext' (hex string) and 'key_type' (public/private) in the JSON request.
#     Returns the decrypted message.
#     """
#     data = request.json
#     ciphertext_hex = data['ciphertext']
#     key_type = data['key_type']

#     private_key, public_key = rsa_cipher.load_keys()

#     key = None
#     if key_type == 'public':
#         key = public_key
#     elif key_type == 'private':
#         key = private_key
#     else:
#         return jsonify({'error': 'Invalid key type'}), 400 # Added status code for error

#     # Convert hexadecimal string back to bytes for decryption
#     ciphertext = bytes.fromhex(ciphertext_hex)
#     decrypted_message = rsa_cipher.decrypt(ciphertext, key)
#     return jsonify({'decrypted_message': decrypted_message})

# @app.route('/api/rsa/sign', methods=['POST'])
# def rsa_sign_message():
#     """
#     Signs a message using the RSA private key.
#     Expects 'message' in the JSON request.
#     Returns the signature in hexadecimal format.
#     """
#     data = request.json
#     message = data['message']
#     private_key, _ = rsa_cipher.load_keys() # Only private key is needed for signing

#     signature = rsa_cipher.sign(message, private_key)
#     signature_hex = signature.hex()
#     return jsonify({'signature': signature_hex})

# @app.route('/api/rsa/verify', methods=['POST'])
# def rsa_verify_signature():
#     """
#     Verifies a message signature using the RSA public key.
#     Expects 'message' and 'signature' (hex string) in the JSON request.
#     Returns a boolean indicating if the signature is verified.
#     """
#     data = request.json
#     message = data['message']
#     signature_hex = data['signature']
#     _, public_key = rsa_cipher.load_keys() # Only public key is needed for verification

#     signature = bytes.fromhex(signature_hex)
#     is_verified = rsa_cipher.verify(message, signature, public_key)
#     return jsonify({'is_verified': is_verified})

# Thêm đoạn này trước hàm main
# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)