x = float(input("Entrez un nombre supérieur à 1 : "))

if x <= 1:
    print("Veuillez entrer un nombre supérieur à 1.")
else:
    somme = 0
    N = 0

    while somme <= x:
        N += 1
        somme += N

    if somme > x:
        N -= 1

    print(f"Le plus grand nombre N tel que la somme de 0 à N soit inférieure ou égale à {x} est : {N}")