#make a function to sort a sorted list with a comparaison ( bubble)
l = [4,8,7,2]

def TriParBulle(l):
    nb_permut=1
    while nb_permut !=0:
        nb_permut=0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                a = l[i]
                l[i]=l[i+1]
                l[i+1]=a
                nb_permut +=1

print(l)
TriParBulle(l)
print(l)