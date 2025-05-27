from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route hiển thị giao diện Caesar
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


# Route xử lý mã hóa Caesar
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f'Text: {text}<br>Key: {key}<br>Encrypted Text: {encrypted_text}'


# Route xử lý giải mã Caesar
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f'Text: {text}<br>Key: {key}<br>Decrypted Text: {decrypted_text}'


# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
