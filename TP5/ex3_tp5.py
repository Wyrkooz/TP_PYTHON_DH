def est_palindrome(phrase):
    def nettoyer_phrase(phrase):
        return ''.join(caractere.lower() for caractere in phrase if caractere.isalpha())

    phrase_epuree = nettoyer_phrase(phrase)
    return phrase_epuree == phrase_epuree[::-1]

entree = input("Entrez un mot ou une phrase : ")

if est_palindrome(entree):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")