import random
from univers import maison,personnage
from utils import input_utils


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {"nom" : maison,
            "score" : 0,
            "a_marque": 0,
            "a_stoppe": 0,
            "attrape_vifdor": False,
              }
    joueurs = equipe_data[maison]["joueurs"]
    if est_joueur and joueur :
        new_joueur = [f"{joueur["Prenom"]} {joueur["Nom"]} (Attrapeur)"]
        for i in joueurs[1:]:
            if i.split(" (")[0] != f"{joueur["Prenom"]} {joueur["Nom"]}":
                new_joueur.append(i)
        joueurs = new_joueur
    equipe["joueurs"] = joueurs
    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1,10)
    if proba_but > 5 :
        if joueur_est_joueur == True:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = equipe_attaque["joueurs"][random.randint(0,6)]
        equipe_attaque["score"] += 1
        equipe_attaque["a_marque"] += 1
        print(buteur, " marque un but pour ",equipe_attaque["nom"])
    else:
        equipe_defense["a_stoppe"] += 1
        print(equipe_defense["nom"], "bloque l'attaque !")

def apparition_vifdor():
    if random.randint(1,6) == 6:
        return True
    return False

def attraper_vifdor(e1,e2):
    gagnant = random.choice([e1,e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    return gagnant

def afficher_score(e1,e2):
    print("Score actuel :\n")
    print(f"--{e1["nom"]} : {e1["score"]} points\n")
    print(f"--{e2["nom"]} : {e2["score"]} points")

def afficher_equipe(maison,equipe):
    print("Équipe de ",maison," :\n")
    for i in equipe["joueurs"]:
        print(f" - {i}\n")

def match_quidditch(joueur,maisons):
    equipes = input_utils.load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur["Maison"]
    maison_adverse = joueur["Maison"]
    while maison_adverse == maison_joueur:
        maison_adverse = random.choice(list(maisons.keys()))
    equipe_joueur = creer_equipe(maison_joueur,equipes,True,joueur)
    equipe_adverse = creer_equipe(maison_adverse,equipes,False,None)
    afficher_equipe(maison_joueur,equipe_joueur)
    afficher_equipe(maison_adverse,equipe_adverse)
    print(f"\nTu joues pour {maison_joueur} en tant qu'Attrapeur\n")
    tours = 1
    gagnant_vif = False
    while tours <= 20 :
        print(f"━━━ Tour {tours} ━━━")
        tentative_marque(equipe_adverse,equipe_joueur,False)
        tentative_marque(equipe_joueur, equipe_adverse, True)
        print('\n')
        afficher_score(equipe_joueur,equipe_adverse)
        if apparition_vifdor():
            gagnant = attraper_vifdor(equipe_joueur,equipe_adverse)
            print(f"La Vif d'Or a été attrapé par {gagnant["nom"]} ! (+150 points)\n")
            gagnant_vif = True
            break
        tours += 1
        input("\nAppuyez sur Entrée pour continuer")
    print("Fin du match !")
    afficher_score(equipe_joueur,equipe_adverse)
    print("Résultat final :\n")
    if gagnant_vif:
        print(f"Le Vif d’Or a été attrapé par Serdaigle !\n+150 points pour {gagnant["nom"]} ! Total : {gagnant["score"]} points.\n")
    if equipe_joueur["score"] > equipe_adverse["score"]:
        print(f"La maison gagnante est {equipe_joueur["nom"]} avec {equipe_joueur["score"]} points !\n")
        maison.actualiser_points_maison(maisons,maison_joueur,500)
        print(f"+500 points pour {equipe_joueur["nom"]} Total : {maisons[maison_joueur]}\n")
        print(f"La maison gagnante est {equipe_joueur["nom"]} avec {maisons[maison_joueur]} !\n")
    elif equipe_adverse["score"] > equipe_joueur["score"]:
        print(f"La maison gagnante est {equipe_adverse["nom"]} avec {equipe_adverse["score"]} points !\n")
        maison.actualiser_points_maison(maisons, maison_adverse, 500)
        print(f"+500 points pour {equipe_adverse["nom"]} Total : {maisons[maison_adverse]}\n")
        print(f"La maison gagnante est {equipe_adverse["nom"]} avec {maisons[maison_adverse]} !\n")
    else:
        print(f"Match nul ! Le score est {equipe_joueur["score"]} à {equipe_joueur["score"]}")

def lancer_chapitre4_quidditch(joueur,maisons):
    print("Partie 2 : La grande conclusion de l'aventure\n")
    match_quidditch(joueur,maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    maison.afficher_maison_gagnante(maisons)
    personnage.afficher_personnage(joueur)

