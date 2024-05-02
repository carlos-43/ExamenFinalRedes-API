from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/decrypt_image', methods=['POST'])
def decrypt_image():
    data = request.json
    encrypted_image = data['encrypted_image']
    key = data['key']
    cipher = Fernet(key)
    decrypted_image = cipher.decrypt(encrypted_image)

    with open('decrypted_image.jpg', 'wb') as f:
        f.write(decrypted_image)

    return 'Imagen desencriptada guardada como decrypted_image.jpg'

if __name__ == '__main__':
    app.run(port=8000)
