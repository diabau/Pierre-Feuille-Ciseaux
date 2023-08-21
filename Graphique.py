from tkinter import *
from random import *
import time

# On crée la fenetres 
fenetre = Tk()
fenetre.title("Pierre Feuille Ciseaux")
fenetre.minsize(450,400)

#random
list = ["choixciseaux","choixfeuille","choixpierre"]
random = choice(list)

#déclarations des image et de la valeurs nulle
imageciseaux = PhotoImage(file="graphique\ciseaux.png")
imagepierre = PhotoImage(file="graphique\pierre.png")
imagefeuille = PhotoImage(file="graphique\peuille.png")


choix = "0"






# les actions du boutons

def ciseaux():
    global choix
    choix="choixciseaux"
    if random == "choixfeuille":
        print("Tu as gagné l'adversaire a joué :",random)
        test1 = Label(fenetre, image=imagefeuille).place(x=250, y=125)
        gagné = Label(fenetre, text="Tu as gagné").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)
    elif random == "choixciseaux":
        print("Égalité, l'adversaire a joué :", random)
        test3 = Label(fenetre, image=imageciseaux).place(x=250, y=125)
        égalité = Label(fenetre, text="Vous avez fait égalité").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)
    else:
        print("tu as perdu l'adversaire a joué :",random)
        test2 = Label(fenetre, image=imagepierre).place(x=250, y=125)
        perdu = Label(fenetre, text="Perdu").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)


def pierre():
    global choix
    choix="choixpierre"
    if random == "choixciseaux":
        print("Tu as gagné l'adversaire a joué :",random)
        test3 = Label(fenetre, image=imageciseaux).place(x=250, y=125)
        gagné = Label(fenetre, text="Tu as gagné").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)
    elif random == "choixciseaux":
        print("Égalité, l'adversaire a joué :", random)
        test2 = Label(fenetre, image=imagepierre).place(x=250, y=125)
        égalité = Label(fenetre, text="Vous avez fait égalité").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)
    else:
        test1 = Label(fenetre, image=imagefeuille).place(x=250, y=125)
        print("tu as perdu l'adversaire a joué :",random)
        perdu = Label(fenetre, text="Perdu").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)

    
    

def feuille():
    global choix
    choix='choixfeuille'
    if random == "choixpierre":
        print("Tu as gagné l'adversaire a joué :",random)
        test2 = Label(fenetre, image=imagepierre).place(x=250, y=125)
        gagné = Label(fenetre, text="Tu as gagné").place(x=350, y=325)
        égalité = Label(fenetre, text="Vous avez fait égalité").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)
    elif random == "choixciseaux":
        print("Égalité, l'adversaire a joué :", random)
        test1 = Label(fenetre, image=imagefeuille).place(x=250, y=125)
        fenetre.after(3000, fenetre.destroy)

    else:
        print("tu as perdu l'adversaire a joué :",random)
        test3 = Label(fenetre, image=imageciseaux).place(x=250, y=125)
        perdu = Label(fenetre, text="Perdu").place(x=350, y=325)
        fenetre.after(3000, fenetre.destroy)




# les trois boutons
boutonpierre = Button(fenetre, image=imagepierre, command=pierre)
boutonpierre.grid(row=0,column=0)

boutonfeuille = Button(fenetre, image=imagefeuille, command=feuille)
boutonfeuille.grid(row=1,column=0)

boutonciseaux = Button(fenetre, image=imageciseaux, command=ciseaux)
boutonciseaux.grid(row=2,column=0)

#maintenir la fenetre ouverte

fenetre.mainloop()