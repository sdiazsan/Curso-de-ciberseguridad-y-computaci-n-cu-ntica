from PIL import Image
import numpy as np

# Función para obtener los bits menos significativos (LSB)
def extract_lsb(image_path):
    # Abrir la imagen
    img = Image.open(image_path)
    
    # Convertir la imagen a RGB
    img_rgb = img.convert('RGB')
    
    # Obtener los píxeles
    pixels = np.array(img_rgb)
    
    # Extraer los LSB de cada componente RGB de cada píxel
    lsb_image = pixels & 1  # El operador '& 1' conserva solo el bit menos significativo
    
    return lsb_image

# Función para visualizar los LSB como una nueva imagen
def display_lsb_image(image_path):
    lsb_image = extract_lsb(image_path)
    
    # Mostrar la imagen de los LSB
    img_lsb = Image.fromarray(lsb_image * 255)  # Multiplicar por 255 para hacer los píxeles visibles
    img_lsb.show()

# Ejemplo de uso
image_path = 'imagen_con_mensaje.png'  # Reemplaza con la ruta de la imagen proporcionada
display_lsb_image(image_path)
