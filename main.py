
variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))


if variable == 1:
    from ejers import ejercicio1
elif variable == 2:
    from ejers import ejercicio2
elif variable == 3:
    from ejers import ejercicio3
    ejercicio3()
else:
    print("Introduzca valores entre 1 y 3.")
        
