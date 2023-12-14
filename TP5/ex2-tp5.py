def calcul_moyenne(notes, coefficients):
    if min(notes) < 8:
        return False
    
    somme = sum(note * coef for note, coef in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)
    moyenne = somme / somme_coefficients
    return moyenne

notes = []
coefficients = []

for i in range(5):
    valeurs = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ").split()
    notes.append(float(valeurs[0]))
    coefficients.append(int(valeurs[1]))

moyenne_generale = calcul_moyenne(notes, coefficients)

if moyenne_generale is not False and moyenne_generale > 10:
    print("L'étudiant est admis avec une moyenne générale de", moyenne_generale)
else:
    print("L'étudiant n'est pas admis.")