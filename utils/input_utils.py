import json

def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte != "":
            return texte


def est_entier(s):
    if s == "":
        return False
    if s[0] == "-":
        if len(s) == 1:
            return False
        s = s[1:]
    for c in s:
        if c < '0' or c > '9':
            return False

    return True

def convertir_entier(s):
    negatif = False
    if s[0] == "-":
        negatif = True
        s = s[1:]

    nombre = 0
    for c in s:
        valeur = ord(c) - ord('0')
        nombre = nombre * 10 + valeur

    return -nombre if negatif else nombre


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        if not est_entier(saisie):
            print("Veuillez entrer un nombre entier valide.")
            continue

        nombre = convertir_entier(saisie)

        if (min_val is not None and nombre < min_val) or (max_val is not None and nombre > max_val):
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}")
            continue

        return nombre


def demander_choix(message, options):
    print(message)
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")

    choix = (demander_nombre("Votre choix : ", 1, len(options)))
    return choix

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return json.load(f)
