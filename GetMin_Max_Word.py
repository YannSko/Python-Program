#Find the shorter and the longer word in a sentence


def GetMin_Max_Word(s):
    words=s.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return(min_word, max_word)

s=" La pomme tombe de l'arbre"
min_word, max_word = GetMin_Max_Word(s)
print("Le mot le plus petit est",min_word)
print("Le mot le plus grand est",max_word)