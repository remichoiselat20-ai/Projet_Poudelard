from chapitres import chapitre_1, chapitre_2, chapitre_3, chapitre_4
from utils import input_utils
def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")
    
def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    afficher_menu_principal()
    if input_utils.demander_nombre("", 1, 2) == 1:
        joueur = chapitre_1.lancer_chapitre1()
        chapitre_2.lancer_chapitre_2(joueur)
        chapitre_3.lancer_chapitre_3(joueur, maisons)
        chapitre_4.lancer_chapitre4_quidditch(joueur,maisons)

    else:
        print("bye bye")

lancer_choix_menu()
