import epd2in13
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.clear_frame_memory(0xFF)
# Affichage d'une image noire pour "nettoyer" l'ecran
image = Image.new('1', (128, 255), 1)
epd.set_frame_memory(image, 0, 0)
epd.display_frame()
