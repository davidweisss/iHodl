import epd2in13
import time
import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.clear_frame_memory(0xFF)
# Font
color = 0
police = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
big = ImageFont.truetype(police, 20)
medium = ImageFont.truetype(police, 16)
small = ImageFont.truetype(police, 14)
tiny= ImageFont.truetype(police, 12)

# Generation de l'image a afficher
image = Image.new('1', (255, 128), 1)
draw= ImageDraw.Draw(image)

draw.text((13, 3), 'Erased keys from screen', font =big, fill = 0)
# draw.text((19, 30), 'Date: ' + datetime.datetime.now().strftime("%y-%m-%d %H:%M"), font =tiny, fill = 0)
draw.text((13, 63), 'Disconnect, or wait for a new key', font = medium, fill = 0)
# Sauvegarde de l'image et rotation
image.save('messageRotated.gif')
rotate = Image.open('messageRotated.gif')
result = rotate.rotate(90, expand = 1)
result.save('message.gif')
# Affichage et attente 
epd.set_frame_memory(Image.open('message.gif'), 0, 0)
epd.display_frame()
