import random


def Guess():
    Guess_Number = random.randint(0, 1000)
    i = False
    print(Guess_Number)
    while i ==False:
        
        Try = int(input("Lets find the good number \n"))
        
        if Try < Guess_Number:
            print("You are too Low")
        elif Try > Guess_Number:
            print("You are too High")
        elif Try == Guess_Number:
            print("gg Wp")
            i=True   
            
        


Guess()
