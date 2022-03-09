repet = int(input("Bienvenido \nIntroduzca el número de veces que desee hacer los ejercicios. "))

for i in range(repet):
    
    variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))
    if variable == 1:
        from ejers.ejercicio1 import ejercicio1
    elif variable == 2:
        from ejers.ejercicio2 import ejercicio2
    elif variable == 3:
        from ejers.ejercicio3 import ejercicio3
        ejercicio3()
    else:
        print("Introduzca valores entre 1 y 3.")