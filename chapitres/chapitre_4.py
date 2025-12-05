import random
def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {"nom" : maison,
            "score" : 0,
            "a_marque": 0,
            "a_stoppe": 0,
            "attrape_vifdor": False,
              }
    joueurs = equipe_data[equipe_data.keys()[0]]["joueur"]
    if est_joueur and joueur :
        new_joueur = [f"{joueurs["Prenom"]} {joueur["Nom"]} (Attrapeur)"]
        for i in joueur[1:]:
            if i.slpit(" (")[0] != f"{joueurs["Prenom"]} {joueur["Nom"]}":
                new_joueur.append(i)
        joueurs = new_joueur
    equipe["joueurs"] = joueurs
    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1,10)
