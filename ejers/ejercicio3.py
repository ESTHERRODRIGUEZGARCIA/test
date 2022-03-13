
from random import randint as rd

def ejercicio3():
    def shellSort(arr):
		n = len(arr)
		gap = n//2
        while gap > 0:
			for i in range(gap,n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j-gap] >temp:
					arr[j] = arr[j-gap]
					j -= gap
				arr[j] = temp
			gap = n//2

	arr = []

	while True:
		try:
			rango_inferior = int(input("Rango Inferior: "))
			rango_superior = int(input("Rango Superior: "))

			if rango_superior <= 0 or rango_inferior <= 0:
				print("Sólo se admiten números positivos y mayores que 0. Inténtelo de nuevo")
			elif rango_superior < rango_inferior:
				print("el rango inferior debe ser menor que el superior. Inténtelo de nuevo: ")
			else:
				break

		except:
			print("Mensaje incorrecto. Sólo se aceptan números. Inténtelo de nuevo: ")

	longitud = rd(rango_inferior, rango_superior)

	for i in range(longitud):
		arr.append(rd(0,100))
	print(arr)

	shellSort(arr)
	print(arr)


