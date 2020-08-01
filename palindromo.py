mensaje="""
Bienvenido al mundo de los palindromos.

Por favor introduce una palabra o frase y te diremos si es un palindromo: """

cadena = input(mensaje)
cad1 = cadena.lower().strip().replace(" ","")
cad2 = cad1[::-1]
if cad1 == cad2:
    print('¡Felicidades! ¡¡¡Tu frase es un palindromo!!!!')
else:
    print('Deberias dedicarte a otra cosa')
    print('Eres malo con los palindromos')