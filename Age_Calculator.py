from datetime import datetime

UserYear = int(input('Donne ton année de naissance'))


def Age_Calculator(UserYear):

    Age = datetime.now().year
    Age = Age - UserYear
    print(Age)


Age_Calculator(UserYear)
