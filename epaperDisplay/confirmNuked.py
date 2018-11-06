
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import epd2in13
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

    # Initialisation de l'afficheur
    epd = epd2in13.EPD()
 
        # Initialisation Afficheur (mode partial update)
        epd.init(epd.lut_partial_update)
        image = Image.new('1', (255, 128), 255)
        draw = ImageDraw.Draw(image)
        # Gestion Police
        color = 0
        police = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
        big = ImageFont.truetype(police, 60)
        medium = ImageFont.truetype(police, 25)
        small = ImageFont.truetype(police, 16)
        # Generation de l'image a afficher
        draw.text((10, 0), time.strftime('%H:%M'), font = small, fill = 0)
        draw.text((183, 0), 'WAN '+ str(WAN), font = small, fill = 0)
        draw.text((115, 10), 'jour', font = small, fill = color)
        draw.text((70, 20), str("%.2f" % PERCENT_TOTAL_NOW_FROM_24H), font = big, fill = color)
        draw.text((10, 80), 'heure', font = small, fill = color)
        draw.text((10, 95), str("%.2f" % PERCENT_TOTAL_NOW_FROM_1H), font = medium, fill = color)
        draw.text((95, 80), 'semaine', font = small, fill = color)
        draw.text((95, 95), str("%.2f" % PERCENT_TOTAL_NOW_FROM_7D), font = medium, fill = color)
        draw.text((200, 80), 'base', font = small, fill = color)
        draw.text((193, 95), str("%.2f" % PERCENT_TOTAL_NOW_FROM_BASE), font = medium, fill = color)
        # Sauvegarde de l'image et rotation
        image.save('/opt/coin-ticker/image.jpg')
        rotate = Image.open('/opt/coin-ticker/image.jpg')
        result = rotate.rotate(90, expand = 1)
        result.save('/opt/coin-ticker/result.jpg')
        # Affichage et attente 
        epd.set_frame_memory(Image.open('/opt/coin-ticker/result.jpg'), 0, 0)
        epd.display_frame()
        epd.delay_ms(2000)
        time.sleep(30)

if __name__ == '__main__':
    # Attente de 30s avant de lancer le programme (temps pour le rapberry de se connecter au réseau au démarrage)
    time.sleep(30)
    main()
