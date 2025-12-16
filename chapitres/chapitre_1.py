from utils.input_utils import *
from univers.personnage import *
import json

def introduction():
    with open("chapitres/ascii poudelard.txt","r",encoding="utf-8") as f:
        content = f.read()
        print(f"{content}\n")
    lire("Bonjour mes silly billies", 10)
    input()

def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")
    print("\nChoisissez vos attributs : ")
    traits = ["courage", "intelligence", "loyauté", "ambition"]
    attributs = {}

    for trait in traits:
        while True:
            try:
                v = convertir_entier(input(f"Niveau de {trait} (1-10) : "))
                if 1 <= v <= 10:
                    attributs[trait] = v
                    break
            except:
                pass
    print(attributs)
    joueur = initialiser_personnage(nom, prenom, attributs)
    print()
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    lire("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...ඞ « Cher élève,\nNous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »ඞ", 10)
    if demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]) == 2:
        lire("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:ඞ« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »\nLe monde magique ne saura jamais que vous existiez...", 10)
        lire("Fin du jeu.", 1)
        exit()
    lire("Vous avez intégré Poudelard gg!!ඞ", 1)

def rencontrer_hagrid(personnage):
    lire("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats surle Chemin de Traverse.'", 10)
    if demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"]) == 2:
        lire("Hagrid insiste gentiment et vous entraîne quand même avec lui!", 10)
    

def acheter_fournitures(personnage):
    with open("data/inventaire.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    restants = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    print("\nBienvenue sur le Chemin de Traverse !ඞ")
    print("Catalogue des objets disponibles :")
    for k in sorted(data, key=lambda x: int(x)):
        nom, prix = data[k]
        print(f"\n{k}. {nom} - {prix} galions")
    
    print(f"\n\nVous avez {personnage['Argent']} galions.")

    while restants:
        print("\nObjets obligatoires restant à acheter :", ", ".join(restants))
        choix = input("\nEntrez le numéro de l'objet à acheter : ")
        if choix not in data:
            continue
        nom, prix = data[choix]
        if personnage["Argent"] < prix:
            print("\nVous n'avez pas assez d'argent. Vous perdez la partie.")
            exit()

        modifier_argent(personnage, -prix)
        ajouter_objet(personnage, "Inventaire", nom)

        if nom in restants:
            restants.remove(nom)

        lire(f"Vous avez acheté : {nom} (-{prix} galions).", 10)
        lire(f"Vous avez {personnage['Argent']} galions.ඞ", 10)

    lire("Tous les objets obligatoires ont été achetés !", 10)
    lire("Il est temps de choisir votre animal de compagnie pour Poudlard !", 10)
    lire(f"Vous avez {personnage['Argent']} galions.ඞ", 10)

    animaux = {
        "1": ("Chouette", 20),
        "2": ("Chat", 15),
        "3": ("Rat", 10),
        "4": ("Crapaud", 5)
    }

    lire("Voici les animaux disponibles :", 10)
    for k in animaux:
        nom, prix = animaux[k]
        print(f"\n{k}. {nom} - {prix} galions")

    while True:
        choix = input("Votre choix : ")
        if choix not in animaux:
            continue
        nom, prix = animaux[choix]
        if personnage["Argent"] < prix:
            lire("\nVous n'avez pas assez d'argent. Vous perdez la partie.", 10)
            exit()
        modifier_argent(personnage, -prix)
        ajouter_objet(personnage, "Inventaire", nom)
        lire(f"\nVous avez choisi : {nom} (-{prix} galions).", 10)
        break

    lire("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :", 10)
    afficher_personnage(personnage)

def lancer_chapitre1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    print()
    acheter_fournitures(joueur)
    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    input()
    return joueur
