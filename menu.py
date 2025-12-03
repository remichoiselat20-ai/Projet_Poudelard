from chapitres.chapitre_1 import *
from univers.personnage import *
from chapitres.chapitre_2 import *
from chapitres.chapitre_3 import *
#joueur = lancer_chapitre1()
#lancer_chapitre_2(joueur)
#quiz_magie({'Nom': 'caca', 'Prenom': 'caca', 'Argent': 0, 'Inventaire': ['Baguette magique', 'Robe de sorcier', 'Manuel de potions', 'Chouette'], 'Sortilèges': [], 'Attributs': {'courage': 4, 'intelligence': 11, 'loyauté': 6, 'ambition': 2}, 'Maison': 'Serdaigle'})

def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")
    
def lancer_choix_menu():
    maisons = {
        "Gryffondor" : 0,
        "Serpentard" : 0,
        "Poufsouffle" : 0,
        "Serdaigle" : 0
    }
    afficher_menu_principal()
    if demander_nombre("", 1, 2) == 1:
        joueur = lancer_chapitre1()
        lancer_chapitre_2(joueur)
        lancer_chapitre_3(joueur, maisons)
    else:
        print("bye bye")

lancer_choix_menu()