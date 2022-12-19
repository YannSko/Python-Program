#Compter le nombre de majusucule
#"Bonjour Yann "

def count_upper(s):
    count =0
    for c in s:
        if c.isupper():
            count+=1
    return count

s="Bonjour Yann"

print(count_upper(s))

def count_upper2(s):
    l =[1 if c.isupper() else 0 for c in s]
    total =sum(l)
    return total

def count_upper3(s):
    l= [ 1 for c in s if c.isupper()]
    return len(l)