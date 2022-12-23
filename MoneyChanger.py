#make an ATM

def cash_back_greedy(s, e):
    r = []
    for a in e:
        n = s//a
        r.append(n)
        s -= n*a

    for i in range(len(e)):
        if r[i] > 0:
            print(e[i], "x", r[i])

    if s > 0:
        print("Reste de :", s)
    else:
        print("Toute la monnaie a été rendue")

    return r