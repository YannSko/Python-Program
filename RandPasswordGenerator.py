import random
import string
import os.path


L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  # 25
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  # 51
     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  # 61
     '=', '/', '!', '-', '+', '*', '_', '°', '@', '£', '%', '§', 'µ']  # 74


def ListRandom(L):
    result = ''
    L = L
    for _ in range(2):
        i = random.randint(0, 25)
        result += L[i]

        j = random.randint(26, 51)
        result += L[j]
    
        k = random.randint(52, 61)
        result += L[k]
    
        l = random.randint(62, 74)
        result += L[l]
    return(result)


result = ListRandom(L)

# def RandomPassWord():
#     PasswordGenerate = ""
#     while len(PasswordGenerate) < 9:
# ListRandom(L)


def Register(result):
    UserName = input('Rentrer votre Nom De User\n\n')
    f = open('Mdp_file.txt', 'a',encoding='utf-8')
    f.write("votre user name est" +" " +UserName + '\n')
    f.write("votre mdp est " + str(result)+'\n')
    f.close()


ListRandom(L)
Register(result)
