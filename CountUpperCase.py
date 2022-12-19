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