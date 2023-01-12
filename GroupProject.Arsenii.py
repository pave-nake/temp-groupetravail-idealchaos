# -*- coding: utf-8 *-*

from PIL import Image
import numpy as np
im = Image.open("test.jpg")
im.show()


print(im.format, im.size, im.mode)
largeur, hauteur = im.size
im_new = Image.new("RGB", (largeur+50,hauteur+50))
for x in range(largeur) :
    for y in range(hauteur) :
        pixel=im.getpixel((x,y))
        if (x<50,y>50):
            im_new.putpixel((x+40,y-40),pixel)
        else:
            im_new.putpixel((x-40,y+40),pixel)
        #if (x<50,y<50):
           # im_new.putpixel((x+50,y+50),pixel)
        #else:
           # im_new.putpixel((x-50,y-50),pixel)

im_new.show()

