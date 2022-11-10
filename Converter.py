# Crée des fonctions capable de convertir un integer en string, un integer en float et un float en string
b = int(input())


def Int_To_String(Number):

    print("J'ai"+str(b)+"ans")


def Int_to_Float(Number2):
    print(float(b))
    return b


def Float_to_String(b):
    c = Int_to_Float(b)
    c = str(c)
    print("jai"+c+"ans")


Float_to_String(b)
