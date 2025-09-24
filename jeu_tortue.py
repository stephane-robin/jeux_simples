"""
L'interface est structuree comme suit :
objet affichage_de
objet victoire
objet compte_rebours
objet pen avec objets tortue et lievre
"""
from random import *
import turtle
import time

mauve = "#8E27F5"
couleur_bg = "#F0D3AA"
rouge = "#F54927"
orange = "#F79F23"
vert = "#2EC796"

def dessiner_depart():
    """Dessine la ligne de depart"""
    pen.pendown()
    pen.setposition(0, -100)

def dessiner_arrivee():
    """Dessine le damier a l'arrivee"""
    def dessiner_carre():
        """Dessine un carre noir"""
        pen.pendown()
        pen.fillcolor("black")
        pen.begin_fill()
        for _ in range(4):
            pen.forward(10)
            pen.right(90)
        pen.end_fill()

    def dessiner_ligne_damier(x, y):
        """Dessine une ligne composee de carres noirs et de vides"""
        pen.penup()
        pen.setposition(x, y)
        for _ in range(7):
            dessiner_carre()
            pen.penup()
            pen.right(90)
            pen.forward(20)
            pen.left(90)

    # utilise dessiner_ligne et dessiner_carre pour construire le damier
    dessiner_ligne_damier(300, 50)
    dessiner_ligne_damier(310, 40)

def dessiner_feu(couleur):
    """Dessine les feux tricolores"""
    def dessiner_disque():
        """Dessine un rond entoure d'un cercle noir"""
        pen.pendown()
        pen.fillcolor(couleur)
        pen.begin_fill()
        pen.circle(7)
        pen.end_fill()
        
    pen.penup()
    pen.setposition(0, 100)    
    for _ in range(3):
        dessiner_disque()
        pen.penup()
        pen.forward(20)

def jeu():
    """Sequence de jeu."""
    # le feu est rouge au depart
    dessiner_depart()
    dessiner_arrivee()
    tortue.showturtle()
    lievre.showturtle()
    dessiner_feu(rouge)
    time.sleep(2)
    avancement_tortue = 0
    avancement_lievre = 0
    de = 0
    
    # feu orange clignotant
    for i in range(4):
        compte_rebours.clear()
        if i != 3:
            dessiner_feu(orange)
            compte_rebours.write(3 - i, font=("Arial", 20, "bold"))
            time.sleep(0.3)
            dessiner_feu(couleur_bg)
        else:
            dessiner_feu(vert)
            compte_rebours.write("départ...", font=("Arial", 20, "bold"))
           
    while de != 6 and avancement_tortue != 6:
        titre.write("Tirage du dé : ", font=("Arial", 24, "bold"))
        affichage_de.clear()
        de = randint(1, 6)
        if de == 1:
            affichage_de.shape(image_un)
            affichage_de.showturtle()
        elif de == 2:
            affichage_de.shape(image_deux)
            affichage_de.showturtle()
        elif de == 3:
            affichage_de.shape(image_trois)
            affichage_de.showturtle()
        elif de == 4:
            affichage_de.shape(image_quatre)
            affichage_de.showturtle()
        elif de == 5:
            affichage_de.shape(image_cinq)
            affichage_de.showturtle()
        elif de == 6:
            affichage_de.shape(image_six)
            affichage_de.showturtle()
        time.sleep(1)
        if de == 6:
            # on s'assure que le lievre depasse la ligne d'arrivee lorsqu'il gagne
            lievre.forward(350)
            return "Victoire du lièvre !!!" 
        else:
            avancement_tortue += 1
            tortue.forward(50)  
    # avancement pour que la tortue depasse la ligne d'arrivee lorsqu'elle gagne
    tortue.forward(50)  
    return "Victoire de la tortue !!!"

def creerObjet(x, y, vitesse, couleur, epaisseur):
    """Cree un objet de dessin"""
    objet = turtle.Turtle()
    objet.hideturtle()
    objet.speed(vitesse)
    objet.pensize(epaisseur)
    objet.penup()
    objet.setposition(x, y)
    objet.color(couleur)
    return objet

# creation de la fenetre
screen = turtle.Screen()
screen.setup(width=800, height=570)
screen.title("Jeu du lièvre et de la tortue")
screen.bgcolor(couleur_bg)
image_tortue = "/Users/srobin/Downloads/tortue.gif"
screen.addshape(image_tortue)
image_lievre = "/Users/srobin/Downloads/lievre.gif"
screen.addshape(image_lievre)
image_un = "/Users/srobin/Downloads/un.gif"
screen.addshape(image_un)
image_deux = "/Users/srobin/Downloads/deux.gif"
screen.addshape(image_deux)
image_trois = "/Users/srobin/Downloads/trois.gif"
screen.addshape(image_trois)
image_quatre = "/Users/srobin/Downloads/quatre.gif"
screen.addshape(image_quatre)
image_cinq = "/Users/srobin/Downloads/cinq.gif"
screen.addshape(image_cinq)
image_six = "/Users/srobin/Downloads/six.gif"
screen.addshape(image_six)

# creation d'un objet titre
titre = creerObjet(0, 200, 0, "black", 1)

# creation d'un objet de
affichage_de = creerObjet(200, 220, 0, "black", 1)

# creation d'un objet victoire
victoire = creerObjet(0, 150, 0, mauve, 1)

# creation d'un objet compte_rebours
compte_rebours = creerObjet(80, 96, 0, "black", 1)

# creation d'un objet stylo
pen = creerObjet(0, 50, 0, "black", 3)

# creation d'un objet tortue
tortue = creerObjet(-20, 0, 2, "black", 1)
tortue.shape(image_tortue)

# creation d'un objet lievre
lievre = creerObjet(-20, -50, 2, "black", 1)
lievre.shape(image_lievre)

# programme principal
resultat = jeu()
victoire.write(resultat, font=("Arial", 18, "bold"))

screen.exitonclick()
