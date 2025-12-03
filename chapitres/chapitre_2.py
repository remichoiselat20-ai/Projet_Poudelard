from utils.input_utils import *
from univers.maison import *
from univers.personnage import *

def recontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...\nUn garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    if demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]) == 1:
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:
        joueur["Attributs"]["ambition"] += 1

    print("\nUne fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie ?")
    if demander_choix("Que répondez-vous ?", ["Oui, j’adore apprendre de nouvelles choses ", "Euh… non, je préfère les aventures aux bouquins."]) == 1:
        joueur["Attributs"]["intelligence"] += 1
    else:
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")
    
    print("\nPuis un garçon blond entre avec un air arrogan")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix = demander_choix("Comment réagissez-vous ?", ["Je lui serre la main poliment.", "Je l’ignore complètement.", "Je lui réponds avec arrogance."])
    if choix == 1:
        joueur["Attributs"]["ambition"] += 1
    elif choix == 2:
        joueur["Attributs"]["loyauté"] += 1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
    elif choix == 3:
        joueur["Attributs"]["courage"] += 1

    print("\nLe train continue sa route. Le château de Poudlard se profile à l’horizon...\nTes choix semblent déjà en dire long sur ta personnalité !\n")
    print(f"\nTes attributs mis à jour : {joueur['Attributs']}")


def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    print("\nLa cérémonie de répartition commence dans la Grande Salle\n")
    print("\nLe Choixpeau magique t’observe longuement avant de poser ses questions:\n\n\n")
    gagnante = repartition_maison(joueur, questions)
    print(f"\n\n\nLe Choixpeau s’exclame : {gagnante} !!!\n")
    print(f"\nTu rejoins les élèves de {gagnante} sous les acclamations !")
    joueur["Maison"] = gagnante


def installation_salle_commune(joueur):
    print("\nVous suivez les préfets à travers les couloirs du château...\n")
    with open("data/maisons.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"{data[joueur['Maison']]['emoji']} {data[joueur['Maison']]['description']}")
    print(f"\n{data[joueur['Maison']]['message_installation']}")
    print(f"\nLes couleurs de votre maison : {data[joueur['Maison']]['couleurs'][0]}, {data[joueur['Maison']]['couleurs'][1]}")

def lancer_chapitre_2(joueur):
    recontrer_amis(joueur)
    print("placeholder") # message dumbledore tbd
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    afficher_personnage(joueur)
    print("placeholder") #Affichage d’un message confirmant la fin du chapitre et annonçant le début des cours à Poudlard


