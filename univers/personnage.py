def initialiser_personnage(nom, prenom, attributs):
    personnage = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return personnage


def afficher_personnage(joueur):
    print("Profil du personnage :")
    ordre_cle = ["Nom", "Prenom", "Argent", "Inventaire", "Sortilèges", "Attributs"]
    for cle in ordre_cle:
        if cle not in joueur:
            continue
        valeur = joueur[cle]
        if isinstance(valeur, dict):
            print(f"{cle} :")
            for sous_cle, sous_val in valeur.items():
                print(f" - {sous_cle} : {sous_val}")
        elif isinstance(valeur, list):
            try:
                ligne = ", ".join([str(x) for x in valeur]) if valeur else ""
            except Exception:
                ligne = ""
            print(f"{cle} : {ligne}")
        else:
            print(f"{cle} : {valeur}")

    for cle, valeur in joueur.items():
        if cle in ordre_cle:
            continue
        if isinstance(valeur, dict):
            print(f"{cle} :")
            for sous_cle, sous_val in valeur.items():
                print(f" - {sous_cle} : {sous_val}")
        elif isinstance(valeur, list):
            ligne = ", ".join([str(x) for x in valeur]) if valeur else ""
            print(f"{cle} : {ligne}")
        else:
            print(f"{cle} : {valeur}")


def modifier_argent(joueur, montant):
    if "Argent" not in joueur:
        joueur["Argent"] = 0
    joueur["Argent"] = joueur["Argent"] + montant


def ajouter_objet(joueur, cle, objet):
    if cle not in joueur:
        return
    if not isinstance(joueur[cle], list):
        return
    joueur[cle].append(objet)