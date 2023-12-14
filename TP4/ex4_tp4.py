def most_frequent(lst):
    occurrences = {}

    for element in lst:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    max_element = max(occurrences, key=occurrences.get)
    max_count = occurrences[max_element]

    return max_element, max_count

liste = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
resultat = most_frequent(liste)

print(f"Le nombre le plus frequent dans la liste est le : {resultat[0]} ({resultat[1]}x)")