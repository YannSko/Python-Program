from random import *
from string import *


def ListRandom():
    List = []
    for _ in range(5):
        List.append(randint(0, 10))
        List.append(random(ascii_letters))
        List.append(random(punctuation))
    print(List)


# def RandomPassWord():
#     PasswordGenerate = ""
#     while len(PasswordGenerate) < 9:

ListRandom()
