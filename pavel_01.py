from PIL import Image




def rgb_to_hex(r, g, b):
    r_hex,g_hex,b_hex = hex(r)[2:],hex(g)[2:],hex(b)[2:]
    if len(r_hex) == 1:r_hex = "0" + r_hex
    if len(g_hex) == 1:g_hex = "0" + g_hex
    if len(b_hex) == 1:b_hex = "0" + b_hex
    return(r_hex + g_hex + b_hex)



im = Image.open("space.jpg")
# im.show()

width, height = im.size

im_new = Image.new("RGB", (width, height),) 

# print(im.format, im.size, im.mode)

list=[]
y,x=-1,-1
for y2 in range(height):
        y+=1
        x=0
        for x2 in range(width-1):
                x+=1
                pixel = im.getpixel((x, y))

                r = pixel[0]
                g =  pixel[1]
                b =  pixel[2]
                hexa=rgb_to_hex(r,g,b)
                im_new.putpixel((x,y),(r,g,b))
                list.append(hexa)
im_new.show()
print(list)

########################################################################
#save pixels to new list
def carre(carreSize,middlepoint,pixelslist,imsize,carrepixels=[]):
        mid = middlepoint//2
        w, h = im.size

        X_TL,Y_TL = middlepoint[0]-mid,middlepoint[1]-mid
        
        for i in range(mid*2):
                y=-X_TL



                for o in range(mid*2):

                        x= pixelslist[X_TL]
                        y= X_TL+w








# Modification de la taille de l'image
##image_retaille_1 = image_ini.resize((500, 200), Image.ANTIALIAS)
##image_retaille_1.show()
### ou
##facteur=0.4
##largeur_2 = int(largeur*facteur)
##hauteur_2 = int(hauteur*facteur)
##image_retaille_2 = image_ini.resize((largeur_2, hauteur_2), Image.ANTIALIAS)
##image_retaille_2.show()
