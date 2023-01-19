# -*- coding: utf-8 *-*
from PIL import Image
import numpy as np
im = Image.open("test_2.jpg")
im.show()
def Arsi():


    print(im.format, im.size, im.mode)
    largeur, hauteur = im.size
    im_new = Image.new("RGB", (largeur+50,hauteur+50 ))

    for x in range(0,largeur//2) :
        for y in range(0,hauteur//2) :
           pixel=im.getpixel((x,y))
           im_new.putpixel((x+largeur//2+50,y+hauteur//2+50),pixel)

    for x in range(largeur//2,largeur) :
        for y in range(0,hauteur//2) :
            pixel=im.getpixel((x,y))
            im_new.putpixel((x-largeur//9-50,y+hauteur//2+50),pixel)

    for x in range(largeur//2,largeur) :
        for y in range(hauteur//2,hauteur) :
            pixel=im.getpixel((x,y))
            im_new.putpixel((x-largeur//9-50,y-hauteur//15-35),pixel)

    for x in range(largeur//2) :
        for y in range(hauteur//2,hauteur) :
            pixel=im.getpixel((x,y))
            im_new.putpixel((x+largeur//2+50,y-hauteur//15-35),pixel)
    im_new.save("ediimge.png")
    im_new.show()
