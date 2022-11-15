

def Calcul(a, b, c):

    if a == '+':
        d = b+c
        Resultat(a, b, c, d)
    elif a == '-':
        d = b - c
        Resultat(a, b, c, d)
    elif a == '*':
        d = b*c
        Resultat(a, b, c, d)
    else:
        print('Non Calculable mec')


def Resultat(a, b, c, d):
    print("Le resultat du Calcul de ", b, a, c, "=", d)


# Faire une fonction entrée  qui prends en parametre un string , un int a et un int b et qui envoie les résultats dans la fonction calcul
# la fonction calcul doit être appelé depuis entrée

def Entrée():
    a = input()
    b = int(input())
    c = int(input())
    Calcul(a, b, c)


Entrée()
