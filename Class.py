# '''''''''
# J'ai une classe de nb_élève et mon école comporte 3 matières
# " math "
# " Français "
# " Dessin "

# il y a deux fois plus d'élève en dessin qu'en math
# il y a 10 élèves en français
# Les élèves de math représent la moitié des élèves de français ( ils sont tous en français )


# Afficher le nombre d'élève au total

# ''''
def Ecolier():
    print("Rentrez un NOMBRE D'élèves (un chiffre ou un nombre)")
    Fr = int(input())
    Math = Fr/2
    Dessin = int(Math*2)
    Total = Fr+Dessin
    print("Choisis ta classe ou l'école ( soit  A soit ecole)")
    Choice = str(input())
    if Choice == 'A':
        print("Il y a ", Total, "éleves dans la classeA")
# Il y a une autre classe avec 30 élèves en math ,
# afficher le nombre d'élèves en math , français , dessin et au total

    elif Choice == "ecole":

        Math2 = 30
        Total2 = Math2+Total
        print("Il y a ", Total2, "éleves dans lecole")


Ecolier()
