from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Función para cifrar un mensaje en modo CBC
def encrypt_AES_CBC(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Función para descifrar el mensaje en modo CBC
def decrypt_AES_CBC(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Ejemplo de uso
key = b'16byteslongkey..'  # Clave de 16 bytes
message = "Mensaje secreto: Estoy aprendiendo a cifrar y descifrar con AES"
iv, encrypted_message = encrypt_AES_CBC(message, key)
print("Mensaje cifrado:", encrypted_message)

# Para descifrar
decrypted_message = decrypt_AES_CBC(iv, encrypted_message, key)
print("Mensaje descifrado:", decrypted_message)
