# temp-groupetravail-idealchaos
group projet NSI 1er


arsenii- decoupe image et switch les positions des blocs

anthony- decoupe image et tourne les blocs 

pavel- switch 2 formes de figures sur une image

----------------------------------------------------------------------------------------------------------
veulliez pas modifier le plan de travail 
----------------------------------------------------------------------------------------------------------
OBSOLETE
 for x in range(0,largeur//2) :
        for y in range(0,hauteur//2) :
           pixel=im.getpixel((x,y))
           im_new.putpixel((x+largeur//2+50,y+hauteur//2+50),pixel)
