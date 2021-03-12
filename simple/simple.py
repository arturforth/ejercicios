import random as rd


def gendir(longitud=10):

    res = []

    for i in range(longitud):
        res.append({i:rd.randint(1, 100)})

    return res


rv = gendir()
print('Fin')
