from PIL import Image

# Imagen base
input_image = "hidden_image.png"  # Debe estar en el directorio actual
output_image = "imagen_oculta.png"  # Imagen con el mensaje oculto
message = "Este es el mensaje secreto que debes encontrar."

# Función para ocultar el mensaje en la imagen
def hide_message(image_path, message, output_path):
    # Convertir el mensaje a binario
    binary_message = ''.join(format(ord(c), '08b') for c in message) + '00000000'  # Añadir terminador

    # Cargar la imagen
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Ocultar el mensaje en los últimos bits
    message_index = 0
    new_pixels = []
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modificar solo los 3 primeros canales (RGB)
            if message_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[message_index])
                message_index += 1
        new_pixels.append(tuple(new_pixel))
        if message_index >= len(binary_message):
            break

    # Crear una nueva imagen con los píxeles modificados
    img.putdata(new_pixels)
    img.save(output_path)

# Ejecutar la función para generar la imagen
hide_message(input_image, message, output_image)
print(f"Imagen con mensaje oculto generada: {output_image}")
