from cryptography.fernet import Fernet
import base64

image_path = input("Ingrese la ruta de la imagen: ")

with open(image_path, 'rb') as f:
    image_data = f.read()

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_image = cipher.encrypt(image_data)
encrypted_image_base64 = base64.b64encode(encrypted_image).decode('utf-8')

with open('encrypted_image.jpg', 'wb') as f:
    f.write(encrypted_image)

with open('key.txt', 'wb') as f:
    f.write(key)

print("Imagen encriptada guardada como encrypted_image.jpg")
print("Clave de encriptación guardada en key.txt")
