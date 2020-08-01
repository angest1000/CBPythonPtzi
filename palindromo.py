def palindromo(cadena):
    cad1 = cadena.lower().strip().replace(" ","")
    print(cad1)
    print(cad1[::-1])
    if cad1 == cad1[::-1]:
        return True
    else:
        return False


def main():
    mensaje="""
    Bienvenido al mundo de los palindromos.

    Por favor introduce una palabra o frase y te diremos si es un palindromo: """

    cadena = input(mensaje)
    
    if palindromo(cadena) == True:
        print('\n\n¡Felicidades! ¡¡¡Tu frase es un palindromo!!!!\n\n')
    else:
        print('\n\nDeberias dedicarte a otra cosa')
        print('\nEres malo con los palindromos\n\n')


if __name__ == '__main__':
    main()