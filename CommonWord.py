# Find the common words between 2 sentences


a = "My Name is Yann"
b = "Your name is Yanno"

def CommonWord(a, b):
    words_a = a.lower().split(" ")
    words_b = b.lower().split(" ")

    common_words = []

    for word in words_a:
        if word in words_b:
            common_words.append(word)
    return common_words

print(CommonWord(a, b ))