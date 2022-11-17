import random


def Guess():
    Guess_Number = random.randint(0, 1000)
    i = 0
    print(Guess_Number)
    while i <= 3:
        i += 1
        Try = int(input("Lets find the good number \n"))
        if Try < Guess_Number:
            print("You are too Low")
        if Try > Guess_Number:
            print("You are too High")
        if Try == Guess_Number:
            print("gg Wp")


Guess()
