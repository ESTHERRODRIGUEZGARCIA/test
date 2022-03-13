# Ejercicios de Ordenar
En este repositorio se encuentran resueltos los ejercicios 1, 2 y 3 

La dirección: https://github.com/ESTHERRODRIGUEZGARCIA/test.git

1. Ordenación por inserción dicotómica

Tenemos una tabla de una sola línea donde los componentes serán ordenados por inserción dicotómica.

El código empleado para resolver este ejercicio es el siguiente:

````
def ejercicio1():

    print("La lista que va a ser ordenada es la siguiente: ")
    arr = [55, 74, 1, 31, 28, 10, 34, 19, 45, 93, 100]
    print(arr)
    print("\nLa lista ordenada de mayor a menor es: ")
    arr = [55, 74, 1, 31, 28, 10, 34, 19, 45, 93, 100]
    for i in range (len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
    print(arr)
    
    arr = [55, 74, 1, 31, 28, 10, 34, 19, 45, 93, 100]
    r = []
    for i in range (len(arr)):
        r.append(min(arr))
        arr.remove(min(arr))

    print("\nLa lista ordenada de menor a mayor es: ")            

    print(r)

ejercicio1()

´´´´
El diagrama de flujo:

![image](https://user-images.githubusercontent.com/91721860/158073889-99804dd5-ce09-4c78-a6af-2a8b94b956e5.png)

