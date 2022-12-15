import numpy as np
from numpy import diag


def diagonal():
    arr = np.array([])
    cont = 0
    while cont < 50:
        arr = np.append(arr, cont)
        cont += 1
    arr = np.diag(arr)
    np.save('exercici1.npy', arr)
    return arr


diagonal()
