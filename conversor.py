#Ejercicio de la clase 17 "Modularizando nuestro conversor de monedas" 
# (Tipo de cambio del 31jul2020)
def tipo_peso():
    conv = """Elige el tipo de peso

    1.Peso Mexicano 
    2.Peso Colombiano
    3.Peso Argentino

    Opcion: """
    tip_pso = int(input(conv))
    return tip_pso

def conv_pso_dol(opc):
    if opc == 1:
        val = 22.28
        tip = "Mexicanos"
    elif opc == 2:
        val = 3722.10
        tip = "Colombianos"
    elif opc == 3:
        val = 72.38
        tip = "Argentinos"
    mon = input("Introduzca la cantidad de pesos "+tip+":")
    print("La cantidad es $",round(int(mon)/val,2)," dolares" )


def conv_dol_pso(opc):
    if opc == 1:
        val = 22.28
        tip = "Mexicanos"
    elif opc == 2:
        val = 3722.10
        tip = "Colombianos"
    elif opc == 3:
        val = 72.38
        tip = "Argentinos"
    mon = input("Introduzca la cantidad de dolares: ")
    print("La cantidad es $",round(int(mon)*val,2)," pesos "+tip)

menu  = """Bienvenido al conversor de monedas 💵
Elige una opcion:
1.De peso a dolar
2.De dolar a peso
Opcion:"""
opcion = int(input(menu))

if opcion == 1:
    pso_dol = tipo_peso()

    if pso_dol == 1:
        conv_pso_dol(pso_dol)
    elif pso_dol == 2:
        conv_pso_dol(pso_dol)
    elif pso_dol == 3:
        conv_pso_dol(pso_dol)
    else:
        print('Mi rey, elige un numero entre 1 y 3!!!!')
elif opcion == 2:
    pso_dol = tipo_peso()

    if pso_dol == 1:
        conv_dol_pso(pso_dol)
    elif pso_dol == 2:
        conv_dol_pso(pso_dol)
    elif pso_dol == 3:
        conv_dol_pso(pso_dol)        
    else:
        print('Chiquito: ese no es un numero entre 1 y 3!')
else:
    print('Papi, por favor!!! Te di solo 2 opciones xD')




