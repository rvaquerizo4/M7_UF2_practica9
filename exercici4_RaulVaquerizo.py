import numpy as np

def exercici4Rand():
    arr = np.random.randint(80, size=(3,4))
    print("Primer array 3x4")
    print(arr)
    arr2 = arr
    arr2 = np.reshape(arr,(4,3),order = 'F')
    print ("segundo array 4x3")
    print(arr2)
    return arr

