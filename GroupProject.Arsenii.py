# -*- coding: utf-8 *-*

from PIL import Image
import numpy as np
im = Image.open("images project.jpg")
im.show()


im_new = Image.new("RGB", (512, 504), (128, 128, 128))
largeur, hauteur = im.size

image = np.asarray(im_new)
nb_lignes,nb_colonnes,_ = image.shape

image_sortie = np.copy(im)

Image.fromarray(image).save("image_entree.jpg")
Image.fromarray(image_sortie).save("image_sortie.jpg")

image_entrée = Image.open("images project.jpg")
image = np.asarray(im)

print(image)

Image.fromarray(image).save("output.png")







