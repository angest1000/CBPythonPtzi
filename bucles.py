
def main():

    LIMITE = 1000000
    cont = 0
    potencia = 2**cont
    while(potencia < LIMITE):
        print(f'2 elevado a {cont} es igual a {potencia}')
        cont = cont+1
        potencia = 2**cont

if __name__ == "__main__":
    main()

