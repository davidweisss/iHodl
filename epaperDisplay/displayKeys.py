import epd2in13
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.clear_frame_memory(0xFF)
# Font
color = 0
police = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
big = ImageFont.truetype(police, 60)
medium = ImageFont.truetype(police, 25)
small = ImageFont.truetype(police, 14)
tiny= ImageFont.truetype(police, 12)

# Generation de l'image a afficher
image = Image.new('1', (255, 128), 1)
draw= ImageDraw.Draw(image)
with open('/home/pi/iHodl/public') as f:
            lines = f.read().splitlines()
            
draw.text((13, 3), 'Bitcoin public key', font = tiny, fill = 0)
draw.text((10, 21), lines[0], font = small, fill = 0)
draw.text((10, 38), lines[1], font = small, fill = 0)

with open('/home/pi/iHodl/private') as f:
            lines = f.read().splitlines()
draw.text((13, 63), 'Corresponding bitcoin private key', font = tiny, fill = 0)
draw.text((10, 81), lines[0], font = small, fill = 0)
draw.text((10, 98), lines[1], font = small, fill = 0)
# Sauvegarde de l'image et rotation
image.save('image.jpg')
rotate = Image.open('image.jpg')
result = rotate.rotate(90, expand = 1)
result.save('result.jpg')
# Affichage et attente 
epd.set_frame_memory(Image.open('result.jpg'), 0, 0)
epd.display_frame()
