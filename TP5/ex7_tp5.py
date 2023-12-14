import os.path
import datetime

def verif_fichier(nom_fichier):
    if os.path.isfile(nom_fichier):
        taille = os.path.getsize(nom_fichier)
        date_modification = datetime.datetime.fromtimestamp(os.path.getmtime(nom_fichier))
        return True, taille, date_modification
    else:
        return False, None, None

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

existe1, taille1, date1 = verif_fichier(fichier1)
existe2, taille2, date2 = verif_fichier(fichier2)

if existe1:
    print(f"Le fichier {fichier1} existe, sa taille est de {taille1} octets et sa date de modification est {date1}.")
else:
    print(f"Le fichier {fichier1} n'existe pas.")

if existe2:
    print(f"Le fichier {fichier2} existe, sa taille est de {taille2} octets et sa date de modification est {date2}.")
else:
    print(f"Le fichier {fichier2} n'existe pas.")

if existe1 and existe2:
    if date1 > date2:
        print(f"Le fichier le plus récent est {fichier1}.")
    elif date2 > date1:
        print(f"Le fichier le plus récent est {fichier2}.")
    else:
        print("Les deux fichiers ont été modifiés à la même date.")