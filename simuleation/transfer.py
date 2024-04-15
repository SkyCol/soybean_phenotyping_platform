## transfer png to jpg
from PIL import Image

def convert_png_to_jpg(png_path, jpg_path):
    png_image = Image.open(png_path)

    if png_image.mode != 'RGB':
        png_image = png_image.convert('RGB')

    png_image.save(jpg_path, 'JPEG')

    png_image.close()

png_file = "./images/bg.png"
jpg_file = "./images/bg.jpg"
convert_png_to_jpg(png_file, jpg_file)
