import numpy as np
from numpy import diag

#Importar libreria numpy

#Definir funcion
def diagonal():
    #Declarar array numpy
    arr = np.array([])
    #Contador
    cont = 0
    #Bucle para rellenar la array desde 0 hasta 49
    while cont < 50:
        #Rellenamos la array
        arr = np.append(arr, cont)
        #aumentamos en 1 el contador
        cont += 1
    #Utilizamos el metodo diag para hacer la diagonal
    arr = np.diag(arr)
    #Guardamos nuestra array en el archivo
    np.save('exercici1.npy', arr)
    return arr

