def run():
    mi_diccionario = {
        'usuario': 'Angel',
        'password': 'contraseña',
        'edad': 26
    }

    # print(mi_diccionario['usuario'])
    # print(mi_diccionario['password'])
    # print(mi_diccionario['edad'])


    poblacion_paises = {
        'Argentina':44938712,
        'Brasil':210147125,
        'Colombia':50372424
    }
    # print(poblacion_paises['Bolivia'])

    # print(poblacion_paises.keys())
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    print('\n')
    # print(poblacion_paises.items())
    for pais,pob in poblacion_paises.items():
        print(pais+' tiene '+str(pob)+' habitantes')


if __name__ == '__main__':
    run()