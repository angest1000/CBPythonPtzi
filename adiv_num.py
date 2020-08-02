import random

def main():
    rand = random.randint(1,100)
    num = int(input('Escribe un numero entre 1 y 100: '))
    intentos=1
    print('Intentos: ',intentos)
    while rand != num:
        if num < rand:
            num = int(input('\nElige un numero mas grande: '))
            intentos+=1
            print('Intentos: ',intentos)
        else:
            num = int(input('\nElige un numero mas pequeño: '))
            intentos+=1
            print('Intentos: ',intentos)
    print('\n¡¡¡Felicidades!!! Haz ganado!!! ')

if __name__ == '__main__':
    main()