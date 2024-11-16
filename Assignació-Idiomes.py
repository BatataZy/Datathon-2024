from yogi import *

def assignacio_idiomes(L: list)->list[str]:
    #pongo la L por si acabamos usando una lista con los prefiles de la gente (lista de listas)

    possible_language = [0, 0, 0, 0, 0]
    possible_language_list = ['español', 'catala', 'english', 'francais', 'deutsch']

    for x in range(len(L)):
        #Por si usamos la lista de listas, asignar la persona a x para ver sus datos individualmente
        x = L[x]
        print('perfil individual: ', x)
        a = x[3]
        print('lista de idiomas individual: ', a)
        #a es el índice de idiomas que habla. De ser una lista de idiomas, hace falta volver a asignar una variable a los idiomas para poder acceder a ellos individualmente.
            
        for j in range(len(possible_language)):
        #assignar la gent al idioma particular que parlen
            for i in range(len(a)):
                    if possible_language_list[j] == a[i]:
                        possible_language[j] = possible_language[j] + 1
                #añadir el id de la persona que habla es idioma j
    return possible_language

    
def creació_perfil()->list[str]:
    perfil:list[str] = []

    id = read(str)
    nom = read(str)
    edat = read(str)
    idiomes = creació_lista()

    perfil = [id] + [nom] + [edat] + [idiomes]
    print('perfil:', perfil)

    return perfil

def creació_lista()->list[str]:
    L = ['español', 'catala', 'english']
    return L

def main()->None:
    L = creació_perfil()
    L = [L, L]
    print('lista de listas: ', L)
    lista_idiomas = assignacio_idiomes(L)
    print('recuento de hablantes: ', lista_idiomas)


if __name__ == '__main__':
    main()