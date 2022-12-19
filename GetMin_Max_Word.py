#Find the shorter and the longer word in a sentence


def GetMin_Max_Word(s):
    words = s.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return(min_word, max_word)

#find by alphabetic order
def GetMin_Max_Word2(s):
    words = s.split(" ")
    words.sort()
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return min_word, max_word
s=" la moto roule aussi vite que le camion"
min_word, max_word = GetMin_Max_Word(s)
min_word, max_word = GetMin_Max_Word2(s)
print("Le mot le plus petit est",min_word)
print("Le mot le plus grand est",max_word)