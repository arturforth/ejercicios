import random as rd


def matriz(rango=10, dim=5):
    mat = [[rd.randint(1, rango) for e in range(dim)] for e in range(dim)]

    mat = [[3, 4, 6, 8, 3], [3, 5, 4, 3, 6], [3, 5, 4, 2, 1], [3, 1, 6, 2, 1], [3, 7, 9, 1, 5]]

    coordenadas = verpat(mat)

    return mat


def horpat(mat):
    n = len(mat)
    count = 0

    for i in range(n-1):
        for j in range(n-1):
            if mat[i][j] == mat[i][j]:
                count += 1


def verpat(mat):
    n = len(mat)

    sec = []    # Secuencia en una columna cualquiera
    coord_secs = []   # Coordenadas de las secuencias encontradas en todas las columnas

    for i in range(n-1):    # Busca una secuencia en todas las columnas
        for j in range(n-1):    # Busca una secuencia en la columna i
            if mat[j][i] == mat[j+1][i]:
                sec.append(j)

        if len(sec) == 3:
            coord_secs.append([sec[0], i])
            coord_secs.append([sec[2]+1, i])
        if len(sec) == 4:
            coord_secs.append([sec[0], i])
            coord_secs.append([sec[2]+1, i])
            coord_secs.append([sec[0]+1, i])
            coord_secs.append([sec[3]+1, i])

    return coord_secs


A = matriz()
A
