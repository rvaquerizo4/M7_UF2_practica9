import numpy as np

# Inputs para demanar los valores
b = int(input('ingresa el tamaño del array'))
c = int(input('filas'))
d = int(input('columnas'))
e = int(input('valor numerico minimo'))
f = int(input('valor maximo'))


def gen():
    # array con numeros random por randint y reshapa para el formato
    a = np.random.randint(e, f, size=b).reshape((c, d))

    return a


print(gen())


def valormax():
    print(f'El valor maximo del array es {f}')


print(valormax())


def valormin():
    print(f'El valor maximo del array es {e}')


print(valormin())
