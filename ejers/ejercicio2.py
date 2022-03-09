tareas = {
    "a": 2,
    "b": 1,
    "c": 7,
    "d": 8,
    "e": 13,
    "f": 3
}


lista = [["a", "d"], ["d", "b"] ,["b", "f"], ["f", "e"] ,["e", "c"]]
ordenada = []

def ord(lista):
    for i in lista:
        if tareas[i[0]] < tareas[i[1]]:
            ordenada.append(i[0])
        else:
            ordenada.append(i[1])

ord(lista)

ordenada = list(dict.fromkeys(ordenada))

print(ordenada)