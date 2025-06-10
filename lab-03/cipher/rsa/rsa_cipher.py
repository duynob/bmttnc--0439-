import rsa
import os

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, plaintext_txt, encrypt_btn):
        return rsa.encrypt(plaintext_txt.encode('utf-8'), encrypt_btn)

    def decrypt(self, ciphertext_txt, decrypt_btn):
        try:
            return rsa.decrypt(ciphertext_txt, decrypt_btn).decode('utf-8')
        except rsa.DecryptionError:
            return False

    def sign(self, plaintext_txt, sign_btn):
        return rsa.sign(plaintext_txt.encode('utf-8'), sign_btn, 'SHA-1')

    def verify(self, plaintext_txt, signature_txt, verify_btn):
        try:
            return rsa.verify(plaintext_txt.encode('utf-8'), signature_txt, verify_btn) == 'SHA-1'
        except rsa.VerificationError:
            return False