from PIL import Image

# Abrimos la imagen original
imagen = Image.open('imagen/gojo2.jpg')

# Aseguramos que esté en modo RGB
imagen = imagen.convert('RGB')

# Creamos una nueva imagen RGB del mismo tamaño (necesario para poder usar el metodo getpixel())
gris_manual = Image.new('RGB', imagen.size)

# Recorremos cada píxel y aplicamos la fórmula
for x in range(imagen.width):
    for y in range(imagen.height):
        r, g, b = imagen.getpixel((x, y))
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        # Asignamos el mismo valor a R, G y B para simular gris
        gris_manual.putpixel((x, y), (gray, gray, gray))

# Mostramos la imagen convertida a 
gris_manual.show()