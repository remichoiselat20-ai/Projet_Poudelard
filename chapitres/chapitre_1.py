from utils.input_utils import *
from univers.personnage import *
import json

def introduction():
    with open("chapitres/ascii poudelard.txt","r",encoding="utf-8") as f:
        content = f.read()
        print(f"{content}\n")
    print("Bonjour mes silly billies")
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
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    input()
    print("« Cher élève,\nNous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »")
    input()
    if demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]) == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie:ඞ« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »\nLe monde magique ne saura jamais que vous existiez...")
        print("Fin du jeu.")
        exit()
    print("Vous avez intégré Poudelard gg!!")
    input()

def rencontrer_hagrid(personnage):
    print("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats surle Chemin de Traverse.'")
    if demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"]) == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")
    

def acheter_fournitures(personnage):
    with open("data/inventaire.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    restants = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    print("\nBienvenue sur le Chemin de Traverse !")
    input()
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

        print(f"Vous avez acheté : {nom} (-{prix} galions).")
        print(f"Vous avez {personnage['Argent']} galions.")
        input()

    print("Tous les objets obligatoires ont été achetés !")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {personnage['Argent']} galions.")
    input()

    animaux = {
        "1": ("Chouette", 20),
        "2": ("Chat", 15),
        "3": ("Rat", 10),
        "4": ("Crapaud", 5)
    }

    print("Voici les animaux disponibles :")
    for k in animaux:
        nom, prix = animaux[k]
        print(f"\n{k}. {nom} - {prix} galions")

    while True:
        choix = input("Votre choix : ")
        if choix not in animaux:
            continue
        nom, prix = animaux[choix]
        if personnage["Argent"] < prix:
            print("\nVous n'avez pas assez d'argent. Vous perdez la partie.")
            exit()
        modifier_argent(personnage, -prix)
        ajouter_objet(personnage, "Inventaire", nom)
        print(f"\nVous avez choisi : {nom} (-{prix} galions).")
        break

    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
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