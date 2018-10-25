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
# Gestion Police
color = 0
police = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
big = ImageFont.truetype(police, 60)
medium = ImageFont.truetype(police, 25)
small = ImageFont.truetype(police, 15)
tiny= ImageFont.truetype(police, 13)
# Generation de l'image a afficher
draw.text((13, 3), 'Bitcoin public key', font = tiny, fill = 0)
draw.text((10, 21), '3J98t1WpEZ73CNmQviecrnyiW', font = small, fill = 0)
draw.text((10, 38), 'rnqRhWNL', font = small, fill = 0)

draw.text((13, 63), 'Corresponding bitcoin private key', font = tiny, fill = 0)
draw.text((10, 81), '5Kb8kLf9zgWQnogidDA76MzPL', font = small, fill = 0)
draw.text((10, 98), '6TsZZY36hWXMssSzNydYXYB9K', font = small, fill = 0)
# Sauvegarde de l'image et rotation
image.save('image.jpg')
rotate = Image.open('image.jpg')
result = rotate.rotate(90, expand = 1)
result.save('result.jpg')
# Affichage et attente 
epd.set_frame_memory(Image.open('result.jpg'), 0, 0)
epd.display_frame()
