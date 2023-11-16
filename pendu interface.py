# script mot_de_passe.py
from tkinter import *
from tkinter.messagebox import * # boîte de dialogue

nb_lettres_trouvees = 0
nb_essais=0
tabMotATrouver=""
tabLettreTrouvees=""


def Verification():
    global tabMotATrouver, tabLettreTrouvees, nb_lettres_trouvees, nb_essais

    tabMotATrouver=MotATrouver.get()
    nb_lettres_trouvees = 0
    nb_essais=0
    tabLettreTrouvees="_"*len(tabMotATrouver)
    Label2.config(text=tabLettreTrouvees)
    Label3.config(text="reste 7 tentatives")
    ChampLettre.focus_set()
    Canevas.create_image(0,0,anchor=NW, image=photo1) 
    
def VerificationLettre():
    global tabMotATrouver, tabLettreTrouvees, nb_lettres_trouvees, nb_essais

    # Label2.config(text=tabLettreTrouvees)
    lettre=LettreSaisie.get()
    LettreSaisie.set("")
    ChampLettre.focus_set()

    trouve=False
    for i in range(len(tabMotATrouver)):
        if tabMotATrouver[i]==lettre[0]:
            tabLettreTrouvees=tabLettreTrouvees[:i]+tabMotATrouver[i]+tabLettreTrouvees[i+1:]
            nb_lettres_trouvees+=1
            trouve=True
            if nb_lettres_trouvees==len(tabMotATrouver):
                print("Gagné !!!")
                Label3.config(text="Gagné !!!")
                Canevas.create_image(0,0,anchor=NW, image=photo10) 

                break
    Label2.config(text=tabLettreTrouvees)

    if not trouve:
        nb_essais+=1
        Label3.config(text="reste " + str(7-nb_essais)+ " tentative(s)")
        print("Il vous reste : ", 7-nb_essais," tentatives")

        if nb_essais==1:
            image=photo2
        elif nb_essais==2:
            image=photo3
        elif nb_essais==3:
            image=photo4
        elif nb_essais==4:
            image=photo5
        elif nb_essais==5:
            image=photo6
        elif nb_essais==6:
            image=photo7
        # elif nb_essais==7:
        #     image=photo8
        else:
            image=photo9
            Label3.config(text="Perdu !")
            print("Perdu !")

        Canevas.create_image(0,0,anchor=NW, image=image) 


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Jeu du pendu')


# Image de fond
photo1 = PhotoImage(file="Le-Pendu1.png")
photo2 = PhotoImage(file="Le-Pendu2.png")
photo3 = PhotoImage(file="Le-Pendu3.png")
photo4 = PhotoImage(file="Le-Pendu4.png")
photo5 = PhotoImage(file="Le-Pendu5.png")
photo6 = PhotoImage(file="Le-Pendu6.png")
photo7 = PhotoImage(file="Le-Pendu7.png")
# photo8 = PhotoImage(file="Le-Pendu8.png")
photo9 = PhotoImage(file="Le-Pendu9.png")
photo10 = PhotoImage(file="Le-Pendu10.png")


# Création d'un widget Canvas (zone graphique)
Largeur = 160
Hauteur = 160
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo1)
print("Image de fond (item",item,")")
Canevas.pack()

# item = Canevas.create_image(0,0,anchor=NW, image=photo2)

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Mot cherché ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
MotATrouver= StringVar()
Champ = Entry(Mafenetre, textvariable= MotATrouver, show='*', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Valider)
BoutonValider = Button(Mafenetre, text ='Valider', command = Verification)
BoutonValider.pack(side = LEFT, padx = 5, pady = 5)



# Création d'un widget Label (texte 'Mot de passe')
Label0 = Label(Mafenetre, text = 'Entrez lettre ')
Label0.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
LettreSaisie= StringVar()
ChampLettre = Entry(Mafenetre, textvariable= LettreSaisie, bg ='bisque', fg='maroon')
# ChampLettre.focus_set()
ChampLettre.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Valider)
BoutonValiderLettre = Button(Mafenetre, text ='Valider', command = VerificationLettre)
BoutonValiderLettre.pack(side = LEFT, padx = 5, pady = 5)


# Création d'un widget Label (texte 'Mot de passe')
Label2 = Label(Mafenetre, text = 'lettres trouvées')
Label2.pack(side = BOTTOM, padx = 5, pady = 5)

# Création d'un widget Label (texte 'Mot de passe')
Label3 = Label(Mafenetre, text = 'reste 8 tentatives')
Label3.pack(side = BOTTOM, padx = 5, pady = 5)

Mafenetre.mainloop()
