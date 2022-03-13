
def ord(lista):
    lista = [["a", "d"], ["d", "b"], ["b", "f"],["f", "e"],["e", "c"], ]
    for i in lista:
        if tareas[i[0]] < tareas[i[1]]:
            ordenada.append(i[0])
        else:
            ordenada.append(i[1])

ord(lista)