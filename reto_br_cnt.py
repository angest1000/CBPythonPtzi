#programa que busca los multiplos de 14
#Hasta 100
def main():
    
    i = 1
    while i < 100:
        print(i)
        if i % 14 == 0:
            print('Multiplo de 14')
            cont = input('Continuar Y/N: ')
            if cont.lower() == 'y':
                i += 1
                continue
            else:
                break
            
        i += 1

if __name__ == '__main__':
    main()