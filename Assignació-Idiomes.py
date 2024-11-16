from yogi import *

def creació_perfil()->list[str]:
    perfil:list[str] = []

    id = read(str)
    nom = read(str)
    edat = read(str)
    idiomes = creació_lista()

    perfil = [id] + [nom] + [edat] + [idiomes]
    print('perfil:', perfil)

    return perfil

def assignacio_idiomes(L: list)->list[str]:
    #pongo la L por si acabamos usando una lista con los prefiles de la gente (lista de listas)


    language_speakers = [[],[],[],[],[]]
    possible_language_list = ['español', 'catala', 'english', 'francais', 'deutsch']

    for x in range(len(L)):
            #Por si usamos la lista de listas, asignar la persona a x para ver sus datos individualmente
            x = L[x]
            print('perfil individual: ', x)
            a = x[3]
            print('lista de idiomas individual: ', a)
            #a es el índice de idiomas que habla. De ser una lista de idiomas, hace falta volver a asignar una variable a los idiomas para poder acceder a ellos individualmente.
            id = x[0]
            for j in range(len(language_speakers)):
            #assignar la gent al idioma particular que parlen
                for i in range(len(a)):
                        if possible_language_list[j] == a[i]:
                            language_speakers[j] += [id]
                    #añadir el id de la persona que habla es idioma j
    return language_speakers

def creació_lista()->list[str]:
    L = [read(str), read(str)]
    return L

def main()->None:
    L = creació_perfil()
    M = creació_perfil()
    N = creació_perfil()
    B = creació_perfil()
    L = [L, M, N, B] 
    print('lista de listas: ', L)
    lista_idiomas = assignacio_idiomes(L)
    print('recuento de hablantes: ', lista_idiomas)


if __name__ == '__main__':
    main()