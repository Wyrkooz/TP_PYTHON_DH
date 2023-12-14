import time

n = int(input("Entrez un nombre entier positif : "))

if n <= 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    print(f"Compte à rebours démarré pour {n} :")
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(1)