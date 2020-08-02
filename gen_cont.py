import random
def generar_contrasena(longitud):
    mayus = ['A','B','C','D','E','F','G'
            ,'H','I','J','K','L','M','N'
            ,'Ñ','O','P','Q','R','S','T'
            ,'U','V','W','X','Y','Z']
    minus = ['a','b','c','d','e','f','g'
            ,'h','i','j','k','l','m','n'
            ,'ñ','o','p','q','r','s','t'
            ,'u','v','w','x','y','z'] 
    num = ['0','1','2','3','4','5','6','7','8','9']
    simbolos = ['.',',',':',';','*','{','}'
                ,'[',']','(',')','!','#','$'
                ,'%','&','/','\'','=','¿','?']

    caracteres =  mayus + minus + num + simbolos
    contrasenia = []
    for i in range(longitud):

        car = random.choice(caracteres)
        contrasenia.append(car)

    contrasenia = "".join(contrasenia)

    return contrasenia

def main():
    longitud = int(input('De que longitud quieres que sea tu nueva contraseña: '))
    contrasenia = generar_contrasena(longitud)
    print('Tu nueva contraseña es: '+contrasenia)

if __name__ == '__main__':
    main()