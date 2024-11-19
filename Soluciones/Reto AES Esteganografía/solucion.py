from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ==========================
# Extraer el mensaje cifrado
# ==========================

# Función para extraer datos binarios ocultos en una imagen
def extract_data(image_path, message_length):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    binary_data = ""
    for pixel in pixels:
        for i in range(3):  # Solo consideramos los 3 primeros valores RGB
            binary_data += str(pixel[i] & 1)
            if len(binary_data) >= message_length * 8:  # Detenemos cuando tenemos los bits necesarios
                break
        if len(binary_data) >= message_length * 8:
            break
    
    # Dividimos los datos binarios en bytes
    bytes_data = bytearray()
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            bytes_data.append(int(byte, 2))
    
    return bytes_data

# Longitud conocida del texto cifrado
#message = "El reto final combina AES y esteganografía."
#ciphertext_length = len(pad(message.encode(), AES.block_size))  # Longitud en bytes
#print(ciphertext_length)
ciphertext_length = 48

# Ruta de la imagen con los datos ocultos
input_image = "reto_final.png"  # Imagen generada con los datos ocultos

# Extraemos los datos
ciphertext = extract_data(input_image, ciphertext_length)
print("Texto cifrado extraído (bytes):", ciphertext)

# ==========================
# Descifrar el mensaje
# ==========================

# Configuración de la clave y vector de inicialización
key = b"AES2023".ljust(16, b"0")
iv = b"1234567890123456"

# Descifrar el texto cifrado
cipher = AES.new(key, AES.MODE_CBC, iv)
try:
    message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
    print("Mensaje descifrado:", message)
except ValueError as e:
    print(f"Error al descifrar: {e}")
