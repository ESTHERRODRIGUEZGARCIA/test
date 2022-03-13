
from random import randint as rd

def ejercicio3():
    from Clases import shellShort

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

	print(arr)


