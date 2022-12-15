import numpy as np #importar para la práctica


def crearPrimera():#creación de la primera matriz
    a = np.array([88, 23, 39, 41])
    return a


def crearSegundo():#creación de la segunda matriz
    b = np.array([[76.4, 21.7, 38.4] ,[41.2 , 52.8 , 68.9]]).reshape(1,6)
    return b

def crearTercero(): #creación de la tercera matriz
    c = np.array([12,4,9,8]).reshape(4,1) #reshape da la forma que se pide

    return c


def imprimir():
    print("Primera matriz")
    print("1. Les matrius com les de la imatge d l’exercici 2")
    print(crearPrimera())
    print("2. Número total d’elements")
    print(crearPrimera().size)
    print("3. La dimensió de la matriu")
    print(crearPrimera().ndim)
    print("4. Tipus d’elements interns")
    print(crearPrimera().dtype)
    print("5. El tamany de la matriu")
    print(crearPrimera().itemsize)

    print(" ------------------------")

    print("Segunda matriz")
    print("1. Les matrius com les de la imatge d l’exercici 2")
    print(crearSegundo())
    print("2. Número total d’elements")
    print(crearSegundo().size)
    print("3. La dimensió de la matriu")
    print(crearSegundo().ndim)
    print("4. Tipus d’elements interns")
    print(crearSegundo().dtype)
    print("5. El tamany de la matriu")
    print(crearSegundo().itemsize)

    print(" ------------------------")

    print("Tercera matriz")
    print("1. Les matrius com les de la imatge d l’exercici 2")
    print(crearTercero())
    print("2. Número total d’elements")
    print(crearTercero().size)
    print("3. La dimensió de la matriu")
    print(crearTercero().ndim)
    print("4. Tipus d’elements interns")
    print(crearTercero().dtype)
    print("5. El tamany de la matriu")
    print(crearTercero().itemsize)

    print(" ------------------------")
