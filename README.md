# AutoWarhol #

## Introduction ##

### Objectifs ###

Une artiste sérigraphiste célèbre vient de mourir. Malheureusement, le contenus de ses programmes n'a pas pu être complètement récupéré. Notre mission est de restaurer son 1er programme: AutoWarhol version 1.0 (on y ajoutera une série d'étoiles)

### Démarche logique / mathématique ###

Nous avons commencé par faire une première tentative d’écriture complète d’un code permettant de retrouver un rendu égal à celui attendu. Lorsque-ceci fut effectué, nous avons vérifié si l'on ne pouvais pas simplifier notre code pour le rendre plus lisible. La réflexion globale du groupe fut plus technique qu’abstraite.

## Le programme ##

### Démarche programmation ###

Le programme débute par un zone d’importation incorporant l’ajout du module turtle et du module random, nécessaire au bon fonctionnement du code.

Par la suite, on peut voir s’ajouter une zone de définition des fonctions utiles où l’on introduit les fonctions: maison (qui dessine une maison simple), rue (fonction qui permet de dessiner une rue de maisons: avec des maisons de taille et d'espacement aléatoire), etoile (permet de dessiner une étoile à 5 branches) et enfin ciel_etoile (qui dessine des étoiles aléatoirement  (taille, rotation et emplacement dans le ciel)).

On note que les fonctions définissent le squelette principal du code. En effet c’est elles qui comportent la majeure partie des instructions permettant un affichage optimal: par exemple la taille des maisons adaptées à leur nombre et à la taille de la fenêtre (grâce à la fonction rue). L'introduction du module setpos() sert a placer le stylo sur des coordonées (x,y) combiner cette fonction setpos avec randint permet de défiir une fourchette de coordonées aléatoires où les étoiles n'entreront pas en contact avec les maisons (ce qui revient a définir une fenêtre au dessus de la maison la plus haute).

Les dernières lignes servent à demander à l'utilisateur le nombre de maisons et d'étoiles qu'il souhaite faire afficher et appellent les 2 fonctions rue et ciel_etoile afin de lancer le dessin de ce que l'on souhaite.

Le programme se termine par un module (exitonclick ()) qui permet de terminer le programme en effectuant un clic au sein de la fenêtre de turtle.

### Manuel utilisateur ###

Afin de faire fonctionner le programme et d'afficher le dessin voulu, il suffit à l’utilisateur de lancer le programme, puis de rentrer un nombre entier (<15) pour obtenir un nombre de maisons puis de rentrer un second nombre entier qui déterminera le nombre d'étoiles a dessiner.

### Informations complémentaires ###

Nous avons eu quelques difficultés pour limité les chevauchement des maisons. De plus, il a été compliqué de travailler en groupe (surtout avec 2 personnes en moins). Notre programme n'est donc pas totalement au point (il aurait été préférable de pouvoir le simplifier de nouveau).

