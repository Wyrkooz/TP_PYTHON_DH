inf_10 = 0
entre_10_15 = 0
sup_1 = 0

for i in range(10):
    valeur = float(input("Entrez une valeur entre 0 et 20 : "))
        
    if 0 >= valeur <= 20:
         valeur = float(input("La valeur n'est pas entre 0 et 20 : "))
        
    if valeur < 10:
        inf_10 += 1
    elif 10 <= valeur < 15:
        entre_10_15 += 1
    else:
        supe_1 += 1

print(f"Nombre de valeurs inférieures strictement à 10 : {inf_10}")
print(f"Nombre de valeurs supérieures ou égales à 10 et strictement inférieures à 15 : {entre_10_15}")
print(f"Nombre de valeurs supérieures ou égales à 1 : {sup_1}")