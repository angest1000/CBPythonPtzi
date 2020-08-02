numero = int(input('Introduce un numero: '))
val = 2
while val <= numero / 2:
    if numero % val == 0:
        print(str(val)+' divide a '+str(numero))
    val += 1
else:
    if numero == 1:
        print('No es primo')
    else:
        print('Es un numero primo!!')

