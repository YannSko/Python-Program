def Année_Bisextile():
    Année = int(
        input("Rentrez une année afin de vérifier si elle est bisextile\n"))
    Check = Année % 4
    if Check != 0:
        print("l'Année rentrée n'est pas une année bisextile")
    else:
        print("l'Année rentrée est une année bisextile")


Année_Bisextile()
