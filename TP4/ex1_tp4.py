table = float(input("Vous chercher la table de multiplication de quel nombre ? "))
lst = []
for i in range (10):
    lst.append((table*i))
for i in range ((len(lst))):
    print("{} * {} = {}".format(table, i, lst[i]))