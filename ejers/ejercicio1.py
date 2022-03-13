
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