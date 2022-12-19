#Tri par Sélection

import random

def Random_List(n, min,max):
    l=[]
    for i in range(n):
        e = random.randint(min,max)
        l.append(e)
    return l

def Tri_Selection(l):
    for unsorted_index in range(0,len(l)-1):
        min =l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1,len(l)):
            if l[i]<min:
                min =l[i]
                min_index =i
        l[min_index] = l [unsorted_index]
        l[unsorted_index] = min

l= Random_List(8,0,10)
print("Non Trié",l)
Tri_Selection(l)
print("tRIe:",l)