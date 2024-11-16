def selecció_capitans(L:list) -> None:
    #24 es el último elemento de la lista, la popularidad, si se lo añadimos al final de cada perfil
    #19 es el elemento que describe la cantidad de equipos deseada por cada participante
    votos_equipos = [0,0,0]
    #indica cuánta gente quiere equipos de 2, 3 o 4 respectivamente
    for x in range(len(L)):
        #Por si usamos la lista de listas, asignar la persona a x para ver sus datos individualmente
        x = L[x]
        print('perfil individual: ', x)
        t = x[19]
        print('preferencia de tamaño de equipo: ', t)
        if t == 2:
            votos_equipos[0] += 1
        elif t == 3:
            votos_equipos[1] += 1
        else:
            votos_equipos[2] += 1
            
    rel_2 = votos_equipos[0] / (votos_equipos[0] + votos_equipos[1] + votos_equipos[2])
    rel_3 = votos_equipos[1] / (votos_equipos[0] + votos_equipos[1] + votos_equipos[2])
    rel_4 = votos_equipos[2] / (votos_equipos[0] + votos_equipos[1] + votos_equipos[2])
    n_teams = int((len(L)/2)*rel_2 + (len(L)/3)*rel_3 + (len(L)/4)*rel_4) + 1

    teams_h = {f'team{i+1}': L[i] for i in range(n_teams//2)}

    print(teams_h)

         
         
def ordenar_popularidad(L:list)->list[str]:
    L_ = sorted(L, key=lambda v: v[-1])
    return L_

def main()->None:
    ...

if __name__ == '__main__':
    main()