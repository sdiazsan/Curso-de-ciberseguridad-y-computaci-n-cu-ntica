from PIL import Image

# Imagen con el mensaje oculto
hidden_image = "imagen_oculta.png"

# Función para extraer el mensaje oculto
def reveal_message(image_path):
    # Cargar la imagen
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Extraer los últimos bits
    binary_message = ""
    for pixel in pixels:
        for i in range(3):  # Leer solo los 3 primeros canales (RGB)
            binary_message += str(pixel[i] & 1)

    # Dividir en bloques de 8 bits (un carácter por bloque)
    chars = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
    message = ""
    for char in chars:
        if char == "00000000":  # Terminador
            break
        message += chr(int(char, 2))

    return message

# Mostrar el mensaje oculto
message = reveal_message(hidden_image)
print("Mensaje oculto:", message)
