import re
import hashlib
import json
import os

print("Chemin d'accès du fichier :", os.path.abspath('passwords.json'))


def verifier_mot_de_passe():
    while True:
        mot_de_passe = input("Choisissez un mot de passe : ")

        # Vérification de la longueur
        if len(mot_de_passe) < 8:
            print("Erreur : Le mot de passe doit contenir au moins huit caractères.")
            continue

        # Vérification de la présence d'une lettre majuscule
        if not re.search("[A-Z]", mot_de_passe):
            print("Erreur : Le mot de passe doit contenir au moins une lettre majuscule.")
            continue

        # Vérification de la présence d'une lettre minuscule
        if not re.search("[a-z]", mot_de_passe):
            print("Erreur : Le mot de passe doit contenir au moins une lettre minuscule.")
            continue

        # Vérification de la présence d'un chiffre
        if not re.search("[0-9]", mot_de_passe):
            print("Erreur : Le mot de passe doit contenir au moins un chiffre.")
            continue

        # Vérification de la présence d'un caractère spécial
        if not re.search("[!@#$%^&*]", mot_de_passe):
            print("Erreur : Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
            continue

        print("Le mot de passe est valide.")
        return mot_de_passe

def crypter_mot_de_passe(mot_de_passe):
    sha_signature = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return sha_signature

def enregistrer_mdp(mot_de_passe_valide, mot_de_passe_crypte):
    mdp_stock = {}

    try:
        with open('passwords.json', 'r') as file:
            mdp_stock = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    mdp_stock[mot_de_passe_valide] = mot_de_passe_crypte

    with open('passwords.json', 'w') as file:
        json.dump(mdp_stock, file, indent=4)

def afficher_mdp():
    try:
        with open('passwords.json', 'r') as file:
            mots_de_passe = json.load(file)
            print("Débogage - Contenu lu du fichier :", mots_de_passe)  # Affichage pour le débogage

            if not mots_de_passe:
                print("Aucun mot de passe enregistré.")
                return

            print("Mots de passe enregistrés :")
            for mot_de_passe, hachage in mots_de_passe.items():
                print(f"Mot de passe : {mot_de_passe} - Hachage : {hachage}")

    except FileNotFoundError:
        print("Fichier de mots de passe introuvable.")
    except json.JSONDecodeError:
        print("Erreur de lecture du fichier de mots de passe.")



def menu():
    while True:
        choix = input("Voulez-vous : (1) Saisir un nouveau mot de passe, (2) Afficher les mots de passe, ou (3) Quitter ? ")
        if choix == "1":
            mot_de_passe_valide = verifier_mot_de_passe()
            mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe_valide)
            enregistrer_mdp(mot_de_passe_valide, mot_de_passe_crypte)
        elif choix == "2":
            afficher_mdp()
        elif choix == "3":
            print("Programme terminé.")
            break

# Appel de la fonction menu pour démarrer le programme
if __name__ == "__main__":
    menu()

