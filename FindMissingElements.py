#Trouver les Elements manquants 
# number between 1 and 10 (included)

l=[3,8,4,7,2]

def Get_Missing_Numbers(l,min,max):
    missing =[]
    for i in range(min,max+1):
        if i not in l:
            missing.append(i)
    return missing
print(Get_Missing_Numbers(l,1,10))