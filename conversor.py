#Ejercicio de la clase 13 "Tu primer programa: Conversor de monedas 
# (Tipo de cambio del 31jul2020)

menu  = """Bienvenido al conversor de monedas 💵
Elige una opcion:
1.De peso a dolar
2.De dolar a peso
Opcion:"""
opcion = int(input(menu))

if opcion == 1:
    conv = """Elige el tipo de peso

    1.Peso Mexicano 
    2.Peso Colombiano
    3.Peso Argentino

    Opcion: """
    pso_dol = int(input(conv))

    if pso_dol == 1:
        mon = input("Introduzca la cantidad de pesos Mexicanos:")
        print("La cantidad es $",round(int(mon)/22.28,2)," dolares" )
    elif pso_dol == 2:
        mon = input("Introduzca la cantidad de pesos Colombianos:")
        print("La cantidad es $",round(int(mon)/3722.10,2)," dolares" )
    elif pso_dol == 3:
        mon = input("Introduzca la cantidad de pesos Argentinos:")
        print("La cantidad es $",round(int(mon)/72.38,2)," dolares" )
    else:
        print('Mi rey, elige un numero entre 1 y 3!!!!')
elif opcion == 2:
    conv = """Elige el tipo de peso

    1.Peso Mexicano 
    2.Peso Colombiano
    3.Peso Argentino

    Opcion: """
    pso_dol = int(input(conv))

    if pso_dol == 1:
        mon = input("Introduzca la cantidad de dolares:")
        print("La cantidad es $",round(int(mon)*22.28,2)," pesos Mexicanos")
    elif pso_dol == 2:
        mon = input("Introduzca la cantidad de dolares:")
        print("La cantidad es $",round(int(mon)*3722.10,2)," pesos Colombianos")
    elif pso_dol == 3:
        mon = input("Introduzca la cantidad de dolares:")
        print("La cantidad es $",round(int(mon)*72.38,2)," pesos Argentinos" )
    else:
        print('Chiquito: ese no es un numero entre 1 y 3!')
else:
    print('Papi, por favor!!! Te di solo 2 opciones xD')




