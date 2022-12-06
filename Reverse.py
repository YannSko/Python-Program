#Devoir inverser un string

def reverse_string(str):
    r = ""
    for c in str:
        r = c + r
    return r

s = "Bonjour toto"
print(reverse_string(s))

def reverse_string2(str):
    return s[::-1]

print(reverse_string2(s))