import numpy as np

#construire un tableau
A= np.array([1,2,3])

#Construire un tableau avec des valeurs zero ( 3 lignes et 2 colonnes)
B = np.zeros((3,2))
C= B.ndim
print(B)
print(C)
#construire un tableau centré en 0
D =np.random.randn(3,4)
print(D.size)
print(D)

#linspace = créer un tableau avec np.linspace(début,fin,quantité d'élements répartie façon égale entre fin et début)
#np.arrange ( créer un tableau avec un pas)

#assembler des tableaux  np.hstack (tableau 1, 2) plus de colonne
# np.vstack () 
#np concatenate(tab1,tab2,axis=) 1= hstack 0 = vstack  "" 3d (axis=2)
# reshape