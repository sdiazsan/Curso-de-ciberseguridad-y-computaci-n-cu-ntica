from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import itertools
import string

# Archivo cifrado proporcionado
encrypted_file = "ejercicio2_cifrado.bin"  # Asegúrate de tener este archivo en el mismo directorio

# IV en formato base64 proporcionado
iv_base64 = "koflKnVDanNpv4PCBWAOFw=="  

# Función para corregir el padding de base64 (útil si no es múltiplo de 4)
def fix_base64_padding(b64_string):
    return b64_string + '=' * (4 - len(b64_string) % 4)

# Corregir y decodificar el IV proporcionado
iv_base64 = fix_base64_padding(iv_base64)
iv = base64.b64decode(iv_base64)

# Leer el contenido cifrado del archivo
with open(encrypted_file, "rb") as f:
    ciphertext = f.read()

# Función para intentar descifrar con una clave específica
def decrypt_with_key(key):
    try:
        # Extender la clave de 4 caracteres a 16 bytes (ya se les proporciona)
        key_extended = key.ljust(16, "0")  # Completar con ceros hasta 16 bytes
        cipher = AES.new(key_extended.encode(), AES.MODE_CBC, iv)
        # Intentar descifrar
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
        return decrypted_message
    except (ValueError, UnicodeDecodeError):
        return None

# TODO: Implementar lógica de fuerza bruta
# Sugerencia: Generar combinaciones de claves de 4 caracteres y llamar a la función `decrypt_with_key`
# Puedes usar itertools.product para generar combinaciones de caracteres.

# Cuando encuentres la clave correcta, imprime el mensaje descifrado y la clave encontrada.
print("Implementa la lógica de fuerza bruta para encontrar la clave correcta.")



