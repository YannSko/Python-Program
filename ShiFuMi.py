import random


def ShiFuMi():

    Possibility = ["ciseaux", "pierre", "papier"]
    Player = input("Choisissez parmi pierre, papier, ciseaux \n")
    print(" Pierre Feuille Ciseaux !")
    Opponent = random.randint(0, 3)
    Opponent = Possibility[Opponent]
    print(" L'ordinateur a fait" + " " + Opponent)
    if(Player == "pierre"):
        if(Opponent == "papier"):
            print("Perdu!", Opponent, "recouvre", Player)
        else:
            print("Gagné!", Player, "écrase", Opponent)

    elif(Player == "papier"):
        if(Opponent == "ciseaux"):
            print("Perdu!", Opponent, "cut", Player)

        else:
            print("You win!", Player, "recouvre", Opponent)
    elif(Player == "ciseaux"):
        if(Opponent == "Rock"):
            print("Perdu...", Opponent, "écrase", Player)
        else:
            print("Gagné!", Player, "cut", Opponent)

    if(Player == Opponent):
        print("Egalité!")


ShiFuMi()
