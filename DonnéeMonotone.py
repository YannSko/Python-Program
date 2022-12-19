#même tendance sur l'esemble ( increase / decrease)
#check if it's monotonic value

a = [1,2,3,4]
b = [1,2,1,0]

def IsMonotonicValue(l):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True

print("a:", IsMonotonicValue(a))
print("b:", IsMonotonicValue(b))