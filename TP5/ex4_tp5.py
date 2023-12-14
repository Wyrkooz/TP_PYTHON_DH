def decomposition_argent(somme):
    billet100 = somme // 100
    reste = somme % 100
    billet50 = reste // 50
    reste = reste % 50
    billet10 = reste // 10
    reste = reste % 10
    piece2 = reste // 2
    reste = reste % 2
    piece1 = reste

    return billet100, billet50, billet10, piece2, piece1

somme_argent = int(input("Entrez une somme d'argent en euros : "))

billet100, billet50, billet10, piece2, piece1 = decomposition_argent(somme_argent)

print(f"{somme_argent} euros, c’est donc {billet100} billets de 100, {billet50} de 50, {billet10} de 10, {piece2} pièces de 2 et {piece1} pièce de 1.")