def calcul_salaire(heures_travaillees, salaire_horaire):
    if heures_travaillees <= 160:
        salaire = heures_travaillees * salaire_horaire
    elif heures_travaillees <= 200:
        salaire_base = 160 * salaire_horaire
        heures_supplementaires = heures_travaillees - 160
        salaire = salaire_base + (heures_supplementaires * salaire_horaire * 1.25)
    else:
        salaire_base = 160 * salaire_horaire
        salaire_intermediaire = 40 * salaire_horaire * 1.25
        heures_supplementaires = heures_travaillees - 200
        salaire = salaire_base + salaire_intermediaire + (heures_supplementaires * salaire_horaire * 1.5)
    
    return salaire

heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_par_heure = float(input("Entrez le salaire horaire : "))

salaire_total = calcul_salaire(heures, salaire_par_heure)

print(f"Le salaire total est de {salaire_total} euros.")