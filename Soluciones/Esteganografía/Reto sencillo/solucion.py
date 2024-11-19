from PIL import Image
import numpy as np

# Función para extraer los LSB de una imagen
def extract_lsb(image_path):
    img = Image.open(image_path)
    img_rgb = img.convert('RGB')  # Convertir a RGB
    pixels = np.array(img_rgb)
    lsb_image = pixels & 1  # Extrae los bits menos significativos
    return lsb_image

# Función para comparar la uniformidad de los LSB
def compare_lsb(lsb_image):
    # Calcular la media de los LSB extraídos
    mean_value = np.mean(lsb_image)
    # Si la media es cercana a 0.5, los LSB están distribuidos de forma más aleatoria, lo que indica mensaje oculto
    return mean_value

# Función para extraer el mensaje oculto de los LSB
def extract_hidden_message(lsb_image):
    # Convertir la imagen de LSB en una secuencia de bits
    bits = lsb_image.flatten()
    
    # Convertir los bits en caracteres ASCII (8 bits por cada carácter)
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]  # Tomar un bloque de 8 bits
        byte_str = ''.join(str(bit) for bit in byte)
        try:
            character = chr(int(byte_str, 2))  # Convertir a carácter
            if character == '\0':  # Fin del mensaje
                break
            message += character
        except ValueError:
            break
    
    return message

# Función principal para analizar las dos imágenes
def analyze_images(image1_path, image2_path):
    # Extraer los LSB de ambas imágenes
    lsb_image1 = extract_lsb(image1_path)
    lsb_image2 = extract_lsb(image2_path)
    
    # Comparar la uniformidad de los LSB de cada imagen
    score1 = compare_lsb(lsb_image1)
    score2 = compare_lsb(lsb_image2)
    
    print(f"Imagen 1 LSB Score: {score1}")
    print(f"Imagen 2 LSB Score: {score2}")
    
    # El mensaje oculto probablemente se encuentra en la imagen con la puntuación más cercana a 0.5
    # Una puntuación más cercana a 0.5 indica mayor variabilidad, lo que podría indicar un mensaje oculto
    if abs(score1 - 0.5) < abs(score2 - 0.5):
        print("La Imagen 1 contiene el mensaje oculto.")
        hidden_message = extract_hidden_message(lsb_image1)
    else:
        print("La Imagen 2 contiene el mensaje oculto.")
        hidden_message = extract_hidden_message(lsb_image2)
    
    print("Mensaje oculto:", hidden_message)

# Función principal para ejecutar el análisis
def main():
    image1_path = 'hidden_image.png'  # Ruta de la primera imagen
    image2_path = 'imagen_oculta.png'  # Ruta de la segunda imagen
    
    # Analizar ambas imágenes
    analyze_images(image1_path, image2_path)

# Ejecutar el análisis
if __name__ == "__main__":
    main()
