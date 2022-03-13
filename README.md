# Ejercicios de Ordenar
En este repositorio se encuentran resueltos 3 ejercicios de ordenación de distintas maneras. 

La dirección: https://github.com/ESTHERRODRIGUEZGARCIA/test.git

# 1. Ordenación por inserción dicotómica

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

````

El diagrama de flujo:

![image](https://user-images.githubusercontent.com/91721860/158073913-fc8cb893-c901-4b0a-be69-41a1c8c0f7f2.png)


# 2. Una ordenación topológica

En este ejercicio las tareas definidas serán ordenadas de mayor a menor.

El código empleado: 
````
def ejercicio2():

    tareas = {
        "fregar": 2,
        "cocinar": 1,
        "poner la lavadora": 7,
        "aspirar": 8,
        "limpiar los baños": 13,
        "recoger": 3
    }
    
    lista = [["fregar", "aspirar"], ["cocinar", "recoger"], ["poner la lavadora", "limpiar los baños"]]


    ordenada = []

    from Clases import ord

    ordenada = list(dict.fromkeys(ordenada))

    print(ordenada)

ejercicio2()

````
Diagrama de flujo:

![image](https://user-images.githubusercontent.com/91721860/158074752-444e1321-cb32-42b1-afda-656d0225d419.png)


# 3. Completar las especificaciones

He relacionado este ejercicio con la ordenación por inserción con el Shellsort.

````

from random import randint as rd

def ejercicio3():

    from Clases import shellShort

	while (ejercicio3):
		try:
			rango_inferior = int(input("Rango Inferior: "))
			rango_superior = int(input("Rango Superior: "))

			if rango_superior <= 0 or rango_inferior <= 0:
				print("Sólo se admiten números positivos y mayores que 0. Inténtelo de nuevo: ")
			elif rango_superior < rango_inferior:
				print("El rango inferior debe ser menor que el superior. Inténtelo de nuevo: ")
			else:
				break

		except:
			print("Mensaje incorrecto. Sólo se aceptan números. Inténtelo de nuevo: ")

	longitud = rd(rango_inferior, rango_superior)
	arr = []
	for i in range(longitud):
		arr.append(rd(0,100))
	print(arr)
````

* No me funciona el código.




