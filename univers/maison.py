from utils.input_utils import demander_choix

def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(nom_maison, ":", maisons[nom_maison], "points")
 
def afficher_maison_gagnante(maisons):
    valeurs = []
    for m in maisons:
        valeurs.append(maisons[m])
    maximum = valeurs[0]
    for v in valeurs:
        if v > maximum:
            maximum = v
    gagnantes = []
    for m in maisons:
        if maisons[m] == maximum:
            gagnantes.append(m)
    if len(gagnantes) == 1:
        print("Maison gagnante :", gagnantes[0])
    else:
        print("Maisons ex æquo :", ", ".join(gagnantes))

def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attr = joueur["Attributs"]
    scores["Gryffondor"] = scores["Gryffondor"] + attr["courage"] * 2
    scores["Serpentard"] = scores["Serpentard"] + attr["ambition"] * 2
    scores["Poufsouffle"] = scores["Poufsouffle"] + attr["loyauté"] * 2
    scores["Serdaigle"] = scores["Serdaigle"] + attr["intelligence"] * 2

    for q in questions:
        texte = q[0]
        choix_possibles = q[1]
        maisons_associees = q[2]
        choix = demander_choix(texte, choix_possibles)
        index = 0
        for i in range(len(choix_possibles)):
            if choix_possibles[i] == choix:
                index = i
        maison = maisons_associees[index]
        scores[maison] = scores[maison] + 3

    valeurs = []
    for m in scores:
        valeurs.append(scores[m])
    maximum = valeurs[0]
    for v in valeurs:
        if v > maximum:
            maximum = v
    gagnante = ""
    for m in scores:
        if scores[m] == maximum:
            gagnante = m
            break

    print("Résumé des scores :")
    for m in scores:
        print(m, ":", scores[m], "points")

    return gagnante
