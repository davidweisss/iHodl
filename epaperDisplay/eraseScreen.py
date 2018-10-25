import epd2in13
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.clear_frame_memory(0xFF)
 # Affichage d'une image noire pour "nettoyer" l'ecran
image = Image.new('1', (255, 128), 0)
epd.set_frame_memory(image, 0, 0)
epd.display_frame()
image = Image.new('1', (255, 128), 255)
draw = ImageDraw.Draw(image)
# Sauvegarde de l'image et rotation
image.save('image.jpg')
rotate = Image.open('image.jpg')
result = rotate.rotate(90, expand = 1)
result.save('result.jpg')
# Affichage et attente 
epd.set_frame_memory(Image.open('result.jpg'), 0, 0)
epd.display_frame()
