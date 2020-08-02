# Codigo para probar si un numero es o no primo
# y en caso de no serlo muestra entre que numeros 
#es divisible dicho numero

def main():

    numero = int(input('Introduce un numero: '))
    val = 2
    prim=1
    while val <= numero / 2:
        if numero % val == 0:
            print(str(val)+' divide a '+str(numero))
            prim=0
        val += 1

    if prim == 0:
        print(str(numero)+' no es un numero primo!')
    else:
        print(str(numero)+' es primo!!!')

if __name__ == '__main__':
    main()