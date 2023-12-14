def format_name(name):
    return name.capitalize()

def display_names_in_order(first_person, second_person):
    formatted_first = format_name(first_person['prenom']) + ' ' + format_name(first_person['nom'])
    formatted_second = format_name(second_person['prenom']) + ' ' + format_name(second_person['nom'])
    
    if formatted_first < formatted_second:
        print(formatted_first)
        print(formatted_second)
    elif formatted_first > formatted_second:
        print(formatted_second)
        print(formatted_first)
    else:
        if format_name(first_person['prenom']) < format_name(second_person['prenom']):
            print(formatted_first)
            print(formatted_second)
        else:
            print(formatted_second)
            print(formatted_first)

person1 = {
    'nom': input("Entrez le nom de la première personne : "),
    'prenom': input("Entrez le prénom de la première personne : ")
}

person2 = {
    'nom': input("Entrez le nom de la deuxième personne : "),
    'prenom': input("Entrez le prénom de la deuxième personne : ")
}

display_names_in_order(person1, person2)