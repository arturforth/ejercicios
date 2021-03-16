import random as rd


def gendic(longitud=10):
    rd.seed(0)
    res = []

    for i in range(longitud):
        res.append({'id': i, 'edad': rd.randint(1, 100)})

    return res


def sortdic(lista):

    n = len(lista)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j]['edad'] < lista[j+1]['edad']:
                a = lista[j]
                b = lista[j+1]
                lista[j] = b
                lista[j+1] = a

    print('El id de la persona mas joven es: {}'.format(lista[n-1]['id']))
    print('El id de la persona mas vieja es: {}'.format(lista[0]['id']))

    return lista


# rv = gendic()
# # #
# rv_sorted = sortdic(rv)
