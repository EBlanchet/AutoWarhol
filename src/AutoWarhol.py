from turtle import *
from random import randint

######################################################################
###### Zone de définition des fonctions utiles #######################
######################################################################


def maison(cote):
    """ Doit dessiner une maison simple (carré + triangle par dessus)

    :param cote: longueur des côtés du carré et du triangle
    """
    print("maison(", cote, ")")   # <- ne pas modifier !!!
    # Compléter la fonction ici
    right(30)
    forward(cote)
    right(120)
    forward(cote)
    right(120)
    forward(cote)
    left(90)
    forward(cote)
    left(90)
    forward(cote)
    left(90)
    forward(cote)

def rue(nombre_maisons):
    """ Doit dessiner une rue de maisons aléatoires, espacées aléatoirement
    dans la fenêtre

    :param nb_maisons: le nombre de maisons à dessiner à la suite
    """
    print("rue(", nombre_maisons, ")")   # <- ne pas modifier !!!
    # Compléter la fonction ici
    penup()
    right(180)
    forward(250)
    right(90)
    forward(250)
    backward(500)
    right(90)
    pendown()
    forward(500)
    left(180)
    forward(500)
    i = 0   
    while i < nombre_maisons :
        if nombre_maisons == 1 :
            espace= randint(1,1)
            cote= randint(100,175)
        else :
            espace = randint((375//nombre_maisons//3)-((375//nombre_maisons//3)//3),375//nombre_maisons//3)
            cote = randint(375//nombre_maisons-(375//nombre_maisons//3),375//nombre_maisons)
        right(90)
        forward(cote)
        maison(cote)
        right(180)
        forward(cote)
        left(90)
        forward(espace)
        left(180)
        i = i+1
		
def etoile(diametre, rotation):     # étoile à 5 branches
    """ Doit dessiner une étoile à 5 branches de diamètre donné,
    en partant avec un angle donné

    :param diamètre: diamètre de l'étoile (longueur des segments)
    :param rotation: angle de départ du crayon
    """
    print("etoile(", diametre,",", rotation, ")")   # <- ne pas modifier !!!
    # Compléter la fonction ici
    t = 0
    right(rotation)
    while t < 5 :
        forward(diametre)
        right(144)
        t += 1
    

def ciel_etoile(nombre_etoiles):
    """ Doit produire un ciel étoilé au dessus de la maison en utilisant
    la fonction etoile

    :param nb_etoiles: nombre d'étoiles à dessiner
    """
    print("ciel_etoile(", nombre_etoiles, ")")   # <- ne pas modifier !!!
    # Compléter la fonction ici
    right(90)
    penup()
    if nombre_etoiles == 1 :
        setpos(-250,0)
    else :
        setpos(-250, (-250)+(375//nombre_maisons*2.5))
    z = 0
    while z < nombre_etoiles :
        if nombre_etoiles == 1 :
            setpos(randint(-250,250),randint(0,250))
        else :
            setpos(randint(-250,250),randint(50,250))
        pendown()
        diametre = randint(10,50)
        rotation = randint(0,360)
        etoile(diametre,rotation)
        penup()
        z += 1
        
    
        
############################################################################
##### Zone du programme qui se charge de dessiner votre nuit étoilée #######
############################################################################


nombre_maisons = int(input("Combien de maisons voulez-vous ?  (<15)  "))          	# <- ne pas modifier !!!
nombre_etoiles = int(input("Combien d'étoiles voulez-vous ?  "))					# <- ne pas modifier !!!

setup(600, 600) 	# <- ne pas modifier !!!
# Compléter le programme ici

rue(nombre_maisons)
ciel_etoile(nombre_etoiles)

exitonclick()		# <- ne pas modifier !!!

