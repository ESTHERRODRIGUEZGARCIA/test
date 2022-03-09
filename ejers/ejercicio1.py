arr = [5, 7, 3, 2, 10, 9]
for i in range (len(arr)):
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
print(arr)

arr = [5, 7, 3, 2, 10, 9]
r = []
for i in range (len(arr)):
    r.append(min(arr))
    arr.remove(min(arr))
print(r)