import random

nbr_mystere = random.randint(0, 100)
nbr_essaies = 0
trouve = False

print("Devinez le nombre mystère entre 0 et 100 !")

while not trouve:
    x = int(input("Entrez votre estimation : "))
    nbr_essaies += 1

    if x < nbr_mystere:
        print("Le nombre mystère est plus grand.")
    elif x > nbr_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère {nbr_mystere} en {nbr_essaies} essaies !")
        trouve = True
