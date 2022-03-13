def ord(lista):
    for i in lista:
        if tareas[i[0]] < tareas[i[1]]:
            ordenada.append(i[0])
        else:
            ordenada.append(i[1])

ord(lista)