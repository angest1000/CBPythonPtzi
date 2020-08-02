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

    contrasenia =[]
    for i in range(longitud):

        tipo_car = random.randint(1,4)
        if tipo_car == 1:
            car = mayus[random.randint(0,len(mayus)-1)]
        elif tipo_car ==2:
            car = minus[random.randint(0,len(minus)-1)]
        elif tipo_car ==3:
            car = num[random.randint(0,len(num)-1)]
        else:
            car = simbolos[random.randint(0,len(simbolos)-1)]

        contrasenia.append(car)

    return contrasenia

def main():
    longitud = int(input('De que longitud quieres que sea tu nueva contraseña: '))
    contrasenia = generar_contrasena(longitud)
    print('Tu nueva contraseña es: ')
    print(contrasenia)
if __name__ == '__main__':
    main()