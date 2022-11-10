# Crée une fonction Liste qui prends 1 paramètres
# "L" , L étant la liste ci dessous :
#L = [0,6,4,2,10]
# Je veux que tu me return la liste par ordre croissant soit :
#L = [0,2,4,6,10]
# ATTENTION : Je veux que tu trie la liste avec un algorithme et pas manuellement !
# tips : regarder les algorithme de tri en python
L = [0, 6, 4, 2, 10]


def Sort(L):
    c = 0
    print(len(L))
    for i in range(0, len(L)-1):
        while L[i] > L[i+1]:
            c = L[i]
            L[i] = L[i+1]
            L[i+1] = c
            i = i-1

    print(L)


Sort(L)
