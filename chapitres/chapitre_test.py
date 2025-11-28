import sys
import os
"""shoutout to chat gpt"""
# Add parent directory (Projet_Poudelard) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_utils import demander_texte, demander_nombre
from univers.personnage import initialiser_personnage, afficher_personnage
from univers.maison import repartition_maison

from univers.personnage import initialiser_personnage, afficher_personnage
from univers.maison import repartition_maison
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

nom = demander_texte("Nom du personnage : ")
prenom = demander_texte("Prénom du personnage : ")

courage = demander_nombre("Points de courage : ", 0, 10)
intelligence = demander_nombre("Points d'intelligence : ", 0, 10)
loyaute = demander_nombre("Points de loyauté : ", 0, 10)
ambition = demander_nombre("Points d'ambition : ", 0, 10)

attributs = {
    "courage": courage,
    "intelligence": intelligence,
    "loyauté": loyaute,
    "ambition": ambition
}

joueur = initialiser_personnage(nom, prenom, attributs)

print("\nVotre personnage :")
afficher_personnage(joueur)

maison = repartition_maison(joueur, questions)

print("\nLe Choixpeau a parlé !")
print("Tu appartiens à :", maison)
