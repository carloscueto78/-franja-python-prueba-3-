# Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000 en un archivo llamado numeros_prueba.txt. 
# Luego debe leer desde el archivo esos números y agregarlos a una lista
# modifique o cree una nueva lista que contenga solo los nñumeros impares.
# Finalmente con numpy determinar la dimensión de la lista. Imprimir por consola la lista final y su dimensión.



import numpy as np
import random

def escribir():
    nombre_archivo = "./numeros_prueba.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        for i in range(0, 21):
            numero_aleatorio = random.randint(100, 1000)
            n = str(numero_aleatorio)

def leer():
    numeros = [100, 1000]
    with open("./numeros_prueba.txt","r") as file:
        for n in file:
            numeros.append(int(n))
    numero_impar = [100, 1000]
    for n in numeros:
        if n % 2 != 0:
            numero_impar.append(n)
    return numero_impar

def main ():
    escribir()
    numero_impar = leer()

    print(numero_impar)
    arreglo = np.array(numero_impar)
    print(arreglo.ndim)

if __name__ == '__main__':
    main() 

