import random


def Guess():
    Guess_Number = random.randint(0, 100)
    i = False
    compt=0
    print(Guess_Number)
    while i ==False:
        
        Try = int(input("Lets find the good number \n"))
        compt +=1
        if compt ==7:
            i=True
            print("Fin de la partie mec")
        elif Try < Guess_Number:
            print("You are too Low")
        elif Try > Guess_Number:
            print("You are too High")
        elif Try == Guess_Number:
            print("You Guessed the number in "+str(compt)+"tries")
           
            
        


Guess()
