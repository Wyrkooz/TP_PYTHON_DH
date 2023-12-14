N = int(input("Entrez un entier positif : "))
somme = 0

for i in range(N + 1):
    somme += i
    
print(f"La somme des {N} premiers entiers naturels est : {somme}")