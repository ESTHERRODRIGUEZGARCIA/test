from random import randint as rd

def ejercicio3():
    def shellSort(arr):
		n = len(arr)
		gap = n//2
        while gap > 0:
			for i in range(gap,n):
                temp = arr[i]
                j = i
                
