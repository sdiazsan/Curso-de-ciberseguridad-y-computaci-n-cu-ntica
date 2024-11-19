from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Datos proporcionados
encrypted_file = "reto_complejo2.bin"  # Archivo cifrado proporcionado
iv_base64 = "uLkFf93vKyJ5UC2MwrAzkQ=="  # IV proporcionado en base64

# Función para corregir el padding del IV si es necesario
def correct_base64_padding(data):
    while len(data) % 4 != 0:
        data += "="
    return data

# Convertir el IV de base64 a bytes
iv_base64 = correct_base64_padding(iv_base64)
iv = base64.b64decode(iv_base64)

# Leer el contenido cifrado del archivo
with open(encrypted_file, "rb") as f:
    ciphertext = f.read()

# Función para descifrar con una clave específica
def decrypt_with_key(key):
    try:
        # Crear el cifrador AES en modo CBC con la clave actual
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        # Intentar descifrar y desempaquetar el mensaje
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
        return decrypted_message
    except (ValueError, UnicodeDecodeError):
        # Si falla, significa que la clave no es correcta
        return None

# Realizar fuerza bruta para encontrar la clave correcta
for num in range(10000):
    # Generar la clave en el formato AES#### y extenderla a 16 bytes
    key = f"AES{num:04}".ljust(16, "0")
    # Intentar descifrar con la clave generada
    decrypted_message = decrypt_with_key(key)
    if decrypted_message:
        print(f"Clave encontrada: {key}")
        print(f"Mensaje descifrado: {decrypted_message}")
        break
else:
    print("No se encontró la clave correcta.")



