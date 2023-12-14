minute_ecoule = int(input("Entrer le nombre de minutes écoulées depuis le début du mois"))
jour = (minute_ecoule // 60) // 24
heure = (minute_ecoule // 60) % 24
minute = (minute_ecoule % 60)


print(f"La date associée est : Jour {jour}, Heure {heure}, minute {minute}")

