import time

n = int(input("Entrez un nombre entier positif : "))

if n <= 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    print(f"Compte à rebours démarré pour {n} :")
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)