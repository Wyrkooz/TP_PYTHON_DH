BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de convives :"))

nvFromage = (800 * nbConvives / BASE)
nvEau = (2 * nbConvives / BASE)
nvAil = (2 * nbConvives / BASE)
nvPain = (400 * nbConvives / BASE)

print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut : {} gr de formage, {} dl d'eau, {} gousse d'ail, {} gr de pain".format(nbConvives,nvFromage,nvEau,nvAil,nvPain))