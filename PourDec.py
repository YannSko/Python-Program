import numpy as np

Struct = np.array ([[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]) 
print(Struct)


print(" Choisis une position  dans le 1 er rows")
row1 = int(input())
print(" Choisis une position dans le 2 eme row")
row2 =int(input())
print(" Choisis une position dans le 3 eme row")
row3 =int(input())
Struct[row1,row2, row3] = 1
print (Struct)

