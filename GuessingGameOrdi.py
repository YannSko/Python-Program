import random


def CompGuess():
    Guess_Number = int(input("Lets find the good number entre 0 et 100 \n")) 
    i = False
    compt=0
    print(Guess_Number)
    while i ==False:
        
        Try = random.randint(0, 100)
        compt +=1
        if compt ==7:
            i=True
            print("Fin de la partie mec")
        elif Try < Guess_Number:
            print("You are too Low")
            print(Try)
            Try2 = random.randint(Try,100)
            Try=Try2
        elif Try > Guess_Number:
            print("You are too High")
            print(Try)
            Try2 = random.randint(0,Try)
            Try=Try2
        elif Try == Guess_Number:
            print(Try)
            print("You Guessed the number in "+str(compt)+"tries")
           
            
        


CompGuess()