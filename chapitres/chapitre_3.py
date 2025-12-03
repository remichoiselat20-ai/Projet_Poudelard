import json
import random
from utils.input_utils import * 
from univers.maison import *
from univers.personnage import *

def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    print("\nTu commences tes cours de magie à Poudlard...")
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    obligatoire = {"Offensif" : 0, "Défensif" : 0, "Utilitaire" : 0}
    sorts = []
    while not obligatoire["Offensif"] >=1 or not obligatoire["Défensif"] >= 1 or not obligatoire["Utilitaire"] >= 3:
        sort = random.choice(data)
        print(f"Tu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        obligatoire[sort['type']] += 1
        sorts.append(sort)
        data.remove(sort)
        joueur["Sortilèges"].append(sort["nom"])
        input("Appuie sur Entrée pour continuer...")

    print("\nTu as terminé ton apprentissage de base à Poudlard !\nVoici les sortilèges que tu maîtrises désormais :\n")
    for sort in sorts:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")
    
def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("Bienvenue au quiz de magie de Poudlard !\nRéponds correctement aux 4 questions pour faire gagner des points à ta maison.")
    index = 0
    points = 0
    while index < 4:
        q = random.choice(data)
        if demander_texte(f"{index+1}. {q['question']}\n") == q['reponse']:
            print("Bonne réponse ! +25 points pour ta maison.")
            points += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}")
        index += 1
        data.remove(q)
    
    print(f"Score obtenu : {points} points")
    return points

def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur)
    points = quiz_magie(joueur)
    actualiser_points_maison(maisons, joueur["Maison"], points)
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
    


        
