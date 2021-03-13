import random as rd


def matriz(rango=10, dim=5):
    mat = [[rd.randint(1, rango) for e in range(dim)] for e in range(dim)]

    mat = [[3, 4, 6, 8, 3], [3, 5, 4, 3, 6], [3, 5, 4, 2, 1], [3, 1, 6, 2, 1], [3, 7, 9, 1, 5]]

    n = len(mat)

    for i in range(n-1):
        for j in range(n-1):
            if mat[j][i] == mat[j+1][i]:
                pass

    return mat


def horpat():
    pass


def verpat():
    pass


A = matriz()
A
