def fact_while(n):
    factorielle = 1
    print("Calcul de la factorielle avec while :")
    i = 1
    while i <= n:
        factorielle *= i
        print(f" {i}: {factorielle}")
        i += 1
    return factorielle



def fact_for(n):
    factorielle = 1
    print("Calcul de la factorielle avec for :")
    for i in range(1, n + 1):
        factorielle *= i
        print(f" {i}: {factorielle}")
    return factorielle



choix_boucle = input("Choisissez la boucle à utiliser (while ou for) : ")

if choix_boucle == "while":
    entier = int(input("Entrez un entier pour calculer sa factorielle : "))
    resultat = fact_while(entier)
    print(f"La factorielle de {entier} est : {resultat}")
elif choix_boucle == "for":
    entier = int(input("Entrez un entier pour calculer sa factorielle : "))
    resultat = fact_for(entier)
    print(f"La factorielle de {entier} est : {resultat}")
else:
    print("Choix de boucle non valide. Veuillez choisir 'while' ou 'for'.")