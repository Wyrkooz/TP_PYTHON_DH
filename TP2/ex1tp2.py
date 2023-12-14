x = int(input("Entrez x : "))
y = int(input("Entrez y : "))
print("Valeur avant permutation : ", "x :", x, " et  y :", y)

z = x
x = y
y = z

print("Valeur après permutation : ", "x :", x, " et  y :", y)