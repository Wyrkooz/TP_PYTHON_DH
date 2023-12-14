def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(date):
    if len(date) != 8:
        return False, "Format de date incorrect. La date doit avoir 8 chiffres."

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if jour < 1 or jour > 31:
        return False, "(incorrecte)"

    if mois < 1 or mois > 12:
        return False, "(incorrecte)"

    if mois == 2:
        if est_bissextile(annee):
            if jour < 1 or jour > 29:
                return False, "(incorrecte)"
        else:
            if jour < 1 or jour > 28:
                return False, "(incorrecte)"

    if mois in [4, 6, 9, 11] and (jour < 1 or jour > 30):
        return False, "(incorrecete)"

    return True, "(correcte)"

dates_a_verifier = ["12071923", "31041999", "29022022", "28022002", "31062023", "32052024", "00052022"]

for date in dates_a_verifier:
    est_valide, message = est_date_valide(date)
    print(f"{date} {message}")