nom = 'Herzog'
prenom = 'Diego'
math = 14
anglais = 12
info = 18
promotion = 2023
moy=(math + anglais + info) / 3

print(type(nom))
print(type(prenom))
print(type(math))
print(type(anglais))
print(type(info))
print(type(promotion))

print("L'étudiant {} {}, de la promotion {}, a une moyenne de {}".format(nom,prenom,promotion,moy))