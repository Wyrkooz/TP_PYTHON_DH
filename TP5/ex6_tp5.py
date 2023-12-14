def taille_chaine(T):
    taille = 0
    for caractere in T:
        if caractere == '\x00':
            break
        taille += 1
    return taille

def pourcentage_voyelles(T):
    voyelles = 'aeiouAEIOU'
    nb_voyelles = sum(1 for caractere in T if caractere in voyelles)
    taille = taille_chaine(T)
    if taille > 0:
        return (nb_voyelles / taille) * 100
    return 0

def est_sous_chaine(T, sous_chaine):
    taille_T = taille_chaine(T)
    taille_sous_chaine = taille_chaine(sous_chaine)
    for i in range(taille_T - taille_sous_chaine + 1):
        if T[i:i + taille_sous_chaine] == sous_chaine:
            return i
    return -1

def occurrences_sous_chaine(T, sous_chaine):
    count = 0
    start = 0
    while True:
        start = est_sous_chaine(T[start:], sous_chaine)
        if start == -1:
            break
        count += 1
        start += 1
    return count

chaine = input("Entrez une chaîne de caractères (max. 100 caractères) : ")

taille = taille_chaine(chaine)
pourcentage = pourcentage_voyelles(chaine)
sous_chaine = 'wagon'
occurrences = occurrences_sous_chaine(chaine, sous_chaine)

print(f"La taille de la chaîne est : {taille}")
print(f"Le pourcentage de voyelles est : {pourcentage}%")
if est_sous_chaine(chaine, sous_chaine) != -1:
    debut_occurrence = est_sous_chaine(chaine, sous_chaine)
    print(f"La sous-chaîne '{sous_chaine}' commence à l'index : {debut_occurrence}")
else:
    print(f"La sous-chaîne '{sous_chaine}' n'est pas présente.")
print(f"Le nombre d'occurrences de la sous-chaîne '{sous_chaine}' est : {occurrences}")