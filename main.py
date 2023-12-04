import re
import hashlib

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
    # Création d'un objet SHA-256
    sha_signature = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return sha_signature

# Appel des fonctions
mot_de_passe_valide = verifier_mot_de_passe()
mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe_valide)
print("Mot de passe crypté:", mot_de_passe_crypte)
