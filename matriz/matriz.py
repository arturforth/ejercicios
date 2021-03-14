import random as rd


def matriz(rango=5, dim=5):
    mat = [[rd.randint(1, rango) for e in range(dim)] for e in range(dim)]

    # mat = [[0, 0, 0, 0, 0], [3, 5, 4, 3, 6], [3, 5, 4, 2, 1], [3, 1, 6, 2, 1], [3, 7, 9, 1, 5]]

    vertical = versec(mat)
    horizontal = horsec(mat)

    return vertical, horizontal


def horsec(mat):
    n = len(mat)

    sec = []    # Secuencia en una fila cualquiera
    coord_secs = []   # Coordenadas de las secuencias encontradas en todas las filas

    for i in range(n-1):    # Busca una secuencia en todas las filas
        for j in range(n-1):    # Busca una secuencia en la fila j
            if mat[i][j] == mat[i][j+1]:
                sec.append(j)

        if len(sec) == 3:
            coord_secs.append([i, sec[0]])
            coord_secs.append([i, sec[2]+1])
        if len(sec) == 4:
            coord_secs.append([i, sec[0]])
            coord_secs.append([i, sec[2]+1])
            coord_secs.append([i, sec[0]+1])
            coord_secs.append([i, sec[3]+1])

        sec.clear()

    return coord_secs


def versec(mat):
    n = len(mat)

    sec = []    # Secuencia en una columna cualquiera
    coord_secs = []   # Coordenadas de las secuencias encontradas en todas las columnas

    for i in range(n-1):    # Recorre todas las columnas
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

        sec.clear()

    return coord_secs

def findsec():
    pass


A = matriz()
A
