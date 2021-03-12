import random as rd


def gendir(longitud=10):

    res = []

    for i in range(longitud):
        res.append({'id':i,'edad':rd.randint(1, 100)})

    return res


def sortdir(lista):

    c = 0

    while 1:
        for i in range(len(lista)-1):
            if lista[i]['edad'] < lista[i+1]['edad']:
                a = lista[i]
                b = lista[i+1]
                lista[i] = b
                lista[i+1] = a
                c += 1
        if c > 0:
            c = 0
        else:
            break

    return lista


rv = gendir()

rv_sorted = sortdir(rv)

print('Fin')
