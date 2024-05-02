# ExamenFinalRedes-API
Repositorio pregunta 5 Examen Final - API

Paso 1 Ejecutar el servidor
pyhton3 servidor.py

En una terminal distinta correr el cliente (paso 2)
python3 cliente.py

Paso 3 desencriptar en una terminal distinta a las anteriores

curl -X POST -H "Content-Type: application/json" -d '{"encrypted_image": "<imagen_encriptada>", "key": "<clave_encriptacion>"}' http://localhost:8000/decrypt_image

Sustituye <imagen_encriptada> con el contenido de encrypted_image.jpg y <clave_encriptacion> con el contenido de key.txt.
