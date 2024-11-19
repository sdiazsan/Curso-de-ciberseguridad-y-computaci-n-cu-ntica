from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import itertools
import string

# Datos proporcionados
encrypted_file = "ejercicio2_cifrado.bin"  # Archivo cifrado proporcionado
iv_base64 = "Ei9zh6WN8cxOYwy35MPpqw=="  # IV proporcionado en base64 (asegúrate de usar el valor correcto)

# Función para corregir el padding de base64
def fix_base64_padding(b64_string):
    return b64_string + '=' * (4 - len(b64_string) % 4)

# Corregir el IV base64 antes de decodificarlo
iv_base64 = fix_base64_padding(iv_base64)
iv = base64.b64decode(iv_base64)

# Leer el contenido cifrado del archivo
with open(encrypted_file, "rb") as f:
    ciphertext = f.read()

# Función para descifrar con una clave específica
def decrypt_with_key(key):
    try:
        # Extender la clave de 4 caracteres a 16 bytes
        key_extended = key.ljust(16, "0")  # Completa con ceros hasta 16 bytes
        cipher = AES.new(key_extended.encode(), AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
        return decrypted_message
    except (ValueError, UnicodeDecodeError):
        return None

# Implementación de fuerza bruta
chars = string.ascii_letters + string.digits  # Todos los caracteres posibles
for key_tuple in itertools.product(chars, repeat=4):  # Genera combinaciones de 4 caracteres
    key = ''.join(key_tuple)  # Convierte la tupla en un string
    decrypted_message = decrypt_with_key(key)
    if decrypted_message:  # Si se descifra con éxito
        print(f"Clave encontrada: {key}")
        print(f"Mensaje descifrado: {decrypted_message}")
        break
else:
    print("No se encontró la clave correcta.")
