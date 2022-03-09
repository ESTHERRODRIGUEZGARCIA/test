from random import randint as rd
def ejercicio3():

	def shellSort(arr):

		# Start with a big gap, then reduce the gap
		n = len(arr)
		gap = n//2

		# Do a gapped insertion sort for this gap size.
		# The first gap elements a[0..gap-1] are already in gapped
		# order keep adding one more element until the entire array
		# is gap sorted
		while gap > 0:

			for i in range(gap,n):

				# add a[i] to the elements that have been gap sorted
				# save a[i] in temp and make a hole at position i
				temp = arr[i]

				# shift earlier gap-sorted elements up until the correct
				# location for a[i] is found
				j = i
				while j >= gap and arr[j-gap] >temp:
					arr[j] = arr[j-gap]
					j -= gap

				# put temp (the original a[i]) in its correct location
				arr[j] = temp
			gap //= 2

	arr = []


	while True:
		try:
			rango_inferior = int(input("Rango Inferior"))
			rango_superior = int(input("Rango Suferior"))

			if rango_superior <= 0 or rango_inferior <= 0:
				print("Numero negativo y break")
			elif rango_superior < rango_inferior:
				print("Inténtale de nuevo: ")
			else:
				break

		except:
			print("Ey")

	longitud = rd(rango_inferior, rango_superior)

	for i in range(longitud):
		arr.append(rd(0,100))
	print(arr)

	shellSort(arr)
	print(arr)

