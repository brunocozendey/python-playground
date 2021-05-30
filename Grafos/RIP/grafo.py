def bfs(grafo, vertice_fonte):
    visitados, fila = set(), [vertice_fonte]
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice])
    return visitados


def componentes_conexas(grafo, v):
    grafos_conexos = []
    vertices_conexos = list(bfs(grafo,v))
    vertices = grafo.keys()
    vertice_nao_verificados = list(vertices - vertices_conexos)
    grafos_conexos.append(vertices_conexos)

    while vertice_nao_verificados != []:
        vertice_busca = vertice_nao_verificados.pop(0)
        vertices_conexos = list(bfs(grafo,vertice_busca))
        grafos_conexos.append(vertices_conexos)
        for vertice in vertices_conexos:
            if vertice in vertice_nao_verificados:
                vertice_nao_verificados.remove(vertice)

    return grafos_conexos

'''
def media_vertices_componente(lista_componentes):
    soma_vertices = 0
    for componente in lista_componentes:
        soma_vertices += len(componente)
    return round(soma_vertices/len(lista_componentes))
'''

def media_vertices_componente(grafo, lista_componentes):
    return len(grafo.keys())//len(lista_componentes)


'''
grafo = [
        [1,2,3],
        [0,2],
        [0,1,3],
        [0,2],
        [5],
        [4]
        ]
'''

grafo = {1: {2, 4}, 2: {1, 3}, 4: {1, 3}, 3: {2, 4}, 5:{6}, 6:{5}, 7:{}}

grafo1 = {1:{2,3}, 2:{1,3}, 3:{1,2}, 4:{5}, 5:{4,6}, 6:{5}, 7:{}, 8:{9,10}, 9:{10,11}, 10:{8,9,12}, 11:{9}, 12:{10}}

grafo2 = {1:{2,5}, 2:{1,3}, 3:{2, 4}, 4:{3,5}, 5:{1,4}, 6:{}, 7:{}, 8:{9,11}, 9:{8,10}, 10:{9,11}, 11:{8,10,12}, 12:{11}}

grafo3 = {1:{2,4}, 2:{1,3}, 3:{2,4}, 4:{1,3}, 5:{6,7,8}, 6:{5,7}, 7:{5,6,8}, 8:{5,7}, 9:{10,11}, 10:{9,11}, 11:{9,10}, 12:{13,16}, 13:{12,14}, 14:{13,15}, 15:{14,16}, 16:{12,15}, 17:{18,22}, 18:{17,19}, 19:{18,20}, 20:{19,21}, 21:{20,22}, 22:{21,17}, 23:{24}, 24:{23}}

grafo4 = {1:{2,4}, 2:{1,3}, 3:{2,4}, 4:{1,3}, 5:{6,7,8}, 6:{5,7}, 7:{5,6,8}, 8:{5,7}, 9:{10,11,12}, 10:{9,11,12}, 11:{9,10,12}, 12:{9,10,11}, 13:{14,16,17}, 14:{13,15,16}, 15:{14,16,17,19}, 16:{13,14,15,18}, 17:{13,15}, 18:{16,19}, 19:{15,18}, 20:{}}

grafo = grafo2

def calcula_componentes_e_media(grafo):
    lista_componentes = componentes_conexas(grafo,1)
    media_vertices = media_vertices_componente(grafo, lista_componentes)
    componentes_media_vertice = componentes_unitarias = 0
    for componente in lista_componentes:
        if len(componente) == media_vertices:
            componentes_media_vertice +=1
        if len(componente) == 1:
            componentes_unitarias +=1
    return len(lista_componentes), media_vertices, componentes_media_vertice, componentes_unitarias 

componentes, media, componentes_igual_media, componentes_unitarias = calcula_componentes_e_media(grafo1)

print("Número de componentes: ",componentes)
print("Média de vertices: ",media)
print("Componentes com Vértices igual a media: ", componentes_igual_media)
print("componentes com um Vértice: ", componentes_unitarias)

        








