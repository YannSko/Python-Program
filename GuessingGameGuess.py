import random

def Guess():
    print("the ordi will find your number")
    testnumb=50
    min=0
    max=100
    i=True
    while i==True:
        print("is it " +str(testnumb)+"?"'\n')
        test=input("low or high")
        if test =="low":
            testnumb =testnumb*1.5
        elif test == "high":
            testnumb = testnumb*0.5

Guess()