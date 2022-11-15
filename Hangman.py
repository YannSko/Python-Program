
def Verification(Mot: str, Letter: str, VieTotal: int, a: str):

    if Letter in Mot:
        print("ok")
        if Letter not in ListLetter:
            ListLetter.append(Letter)
            Victoire(Mot)
            a = a.replace('_', Letter)
            print(a)
    else:
        print("no")
        VieTotal = Vie(VieTotal)
        print(VieTotal)
    return VieTotal


def Victoire(Mot):
    for _ in Mot:
        CompteWin = +1
    if CompteWin == len(Mot):
        print(GG)


def Vie(b: int):
    VieRestante = b-1
    return VieRestante


def ReplaceWord(a, Mot):
    for _ in Mot:
        a = a+('_')
    print(a)
    return a


CompteWin = 0
ListLetter = []
ListMot = []


def Main():
    VieTotal = 10
    a = ''
    Mot = str(input("entrez un mot  \n"))
    a = ReplaceWord(a, Mot)
    while VieTotal != 0:
        Letter = str(input("Donne une lettre pour deviner le mot "))
        while len(Letter) > 1:
            Letter = str(input("Donne une seule lettre stp"))
        VieTotal = Verification(Mot, Letter, VieTotal, a)


Main()
