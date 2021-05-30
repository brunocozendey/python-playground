#!/usr/bin/python
import sys, getopt,json
import numpy as np
from Grafo import Grafo
import ast

barra = "="*30

def menu():
    print(barra)
    print("|       IMPRIME GRAFOS       |")
    print(barra)
    print(barra)
    print("Digite a opção desejada")
    print("1. Carregar grafo existente")
    print("2. Criar um novo grafo")
    print("3. Calcular Componentes e média do grafo.")
    print("4. Gerar matriz de adjacência do grafo de Micielski.")
    print("5. Gerar a coloração gulosa de um grafo.")
    print("6. Verificar se grafo é Euleriano.")

    print("Ou S/s para sair.")
    option = input("Opção:")
    return option

def imprimir_matriz(M):
    print(barra)
    print("Matriz Adjacência = ")
    for i in range(len(M)):
        print(M[i])

def criar_matriz_zeros(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha) 
    return matriz

def espelhar_matriz(M):
    for i in range(len(M)):
        for j in range(i,len(M)):
            M[j][i] = M[i][j]
    return M

def grafo_to_arestas(grafo):
    arestas = [(k, v) for k in grafo.keys() for v in grafo[k]]
    return arestas

def cria_matriz_adjacencia(n):
    M = criar_matriz_zeros(n)
    for i in range(n):
        for j in range(i,n):
            while True:
                try:
                    M[i][j] = int(input('Digite o valor 0/1 da posição [{}][{}] da matriz adjacência:'.format(i,j)))
                    if M[i][j] in [0,1]:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("O valor deve ser 0 ou 1")
    return M

def matriz_to_str(M):
    matriz_str = ""
    for linha in M:
        for letra in linha:
            matriz_str+=str(letra)+","
        matriz_str = matriz_str[:-1] + ";"
    return matriz_str[:-1]


def criar_arquivo_grafo(file_name, estrutura, matriz):
    while True:
        try:
            grafo_file = open("grafos/"+file_name+'.txt', "w", encoding='utf-8')
            grafo_file.seek(0)
            grafo_info = {'nome':file_name, "estrutura":str(estrutura), "matriz":matriz}    
            grafo_file.write(json.dumps(grafo_info))
            
            grafo_file.close()
            break
        except:
            raise FileNotFoundError('Erro ao criar o arquivo!')
        finally:
            grafo_file.close()

def str_to_matriz(matriz):
    return np.matrix(matriz).tolist()

def carrega_arquivo(file_name): 
    try:
        grafo_file = open("grafos/"+file_name+'.txt', "r", encoding='utf-8')
        grafo_file.seek(0)
        grafo_json = json.load(grafo_file)
        grafo = grafo_json

    except:
        raise FileNotFoundError('Arquivo de Grafo não encontrado!')
    finally:
        grafo_file.close()
    return grafo    

def matriz_to_grafo(M):
    arestas = []
    for linha in range(len(M)):
        for coluna in range(len(M)):
            if M[linha][coluna] == 1:
                arestas.append((linha+1,coluna+1))
    g = Grafo(arestas)
    return g

def criar_grafo():
    nome_grafo = input("Digite o nome do grafo: ")
    while True:
        try:
            numero_arestas = int(input("Indique um número de arestas (Valor inteiro): "))
            break
        except ValueError:
            print('O valor precisa ser um inteiro.')
    MA = espelhar_matriz(cria_matriz_adjacencia(numero_arestas))
    estrutura = matriz_to_grafo(MA)
    criar_arquivo_grafo(nome_grafo,estrutura, MA)
    return MA

def grafo_to_matriz(g):
    arestas = g.get_arestas()
    M = criar_matriz_zeros(len(g))
    for va,vb in arestas:
        M[int(va)-1][int(vb)-1] = 1
    return M

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

def media_vertices_componente(grafo, lista_componentes):
    return len(grafo.keys())//len(lista_componentes)

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

def imprime_calcula_componentes_e_media(grafo):
    calcula_componentes_e_media(grafo)
    componentes, media, componentes_igual_media, componentes_unitarias = calcula_componentes_e_media(grafo)
    print(barra)
    print("Informações das componentes do gráfico =")
    print("Número de componentes: ",componentes)
    print("Média de vertices: ",media)
    print("Componentes com Vértices igual a media: ", componentes_igual_media)
    print("componentes com um Vértice: ", componentes_unitarias)

def matriz_grafo_kn(n):
    M = criar_matriz_zeros(n)
    for lin in range(0,n):
        for col in range(0,n):
            if (lin == col):
                M[lin][col] = 0
            else:
                M[lin][col] = 1
    return M

def matriz_grafo_mycielsky(x,w):
    if (x == w):
        return matriz_grafo_kn(w)
    else:
        mycielsky_menos_1 = matriz_grafo_mycielsky(x-1,w)
        num_vertices = (len(mycielsky_menos_1)*2)+1
        M = criar_matriz_zeros(num_vertices)
        for i in range(0,num_vertices):
            for j in range(0,num_vertices):
                if ((i < num_vertices-1) and (j < num_vertices-1)):
                    if ((i>len(mycielsky_menos_1)-1) or (j>len(mycielsky_menos_1)-1)):
                        M[i][j] = mycielsky_menos_1[i-len(mycielsky_menos_1)][j-len(mycielsky_menos_1)]
                    else:
                        M[i][j] = mycielsky_menos_1[i][j]     
                else:
                    if ((i<len(mycielsky_menos_1)) or (j<len(mycielsky_menos_1)) or (j==i)):
                        M[i][j] = 0
                    else:
                        M[i][j] = 1
        return M

def get_grau_max(g):
    M = grafo_to_matriz(g)
    calc_max = lambda a, b: max([a,b])
    grau_max = 0
    for i in range(0,len(M)):
        calcula_grau = 0
        for j in range(0,len(M)):
            calcula_grau += M[i][j]
        grau_max = calc_max(grau_max,calcula_grau)
    return grau_max


def get_neighbor(arestas,v):
    n = []
    for (v1,v2) in arestas:
        if (v1 == v):
            n.append(v2)
    return n
        

def get_coloracao(g):
    vertices = g.get_vertices()
    vertices.sort()
    cores = list(range(2,(get_grau_max(g)+2)))
    c = [0]*len(vertices)
    c[0] = 1
    for i in range(1,len(vertices)):
        aux_cores = cores.copy()
        neighbors = get_neighbor(g.get_arestas(),i+1)
        for n in neighbors:
            if ( c[n-1] in aux_cores):
                aux_cores.remove(c[n-1])
        c[i] = min(aux_cores)
    return c


def is_conexo(g):
    vertices = g.get_vertices()
    for v in vertices:
        grafos_conexos = componentes_conexas(g.get_dict(),v)
        for conj_vertices in grafos_conexos:
            if conj_vertices.sort() == vertices.sort():
                return True
    else:
        return False  
    
def have_grau_par(g):
    vertices = g.get_vertices()
    for v in vertices:
        grau = len(get_neighbor(g.get_arestas(),v))
        if grau%2 != 0:
            return False
    return True

def is_euleriano(g, nome_grafo):
    # G é conexo e cada vertice de G tem grau par
    if(is_conexo(g) and have_grau_par(g)):
        print("O grafo '{}' é Euleriano".format(nome_grafo))
    else:
        print("O grafo '{}' NÃO é Euleriano".format(nome_grafo))

def init():
    arestas = [(1,2),(1,4),(2,1),(2,3),(3,2),(3,4),(4,1),(4,3)]
    grafo = Grafo(arestas)
    MA = grafo_to_matriz(grafo)
    imprimir_matriz(MA)
    criar_arquivo_grafo("ex1", grafo, MA)
    try:
        arquivo = carrega_arquivo("ex1")
        estrutura = ast.literal_eval(arquivo['estrutura'])
        MA = arquivo['matriz']
        grafo = Grafo(grafo_to_arestas(estrutura)) 
        imprimir_matriz(MA)
    except:
        print("ERRO: Problema ao carregar o arquivo!")
#Ex2
    grafo21 = {1:{2,3}, 2:{1,3}, 3:{1,2}, 4:{5}, 5:{4,6}, 6:{5}, 7:{7}, 8:{9,10}, 9:{10,11}, 10:{8,9,12}, 11:{9}, 12:{10}}
    grafo22 = {1:{2,5}, 2:{1,3}, 3:{2, 4}, 4:{3,5}, 5:{1,4}, 6:{6}, 7:{7}, 8:{9,11}, 9:{8,10}, 10:{9,11}, 11:{8,10,12}, 12:{11}}
    grafo23 = {1:{2,4}, 2:{1,3}, 3:{2,4}, 4:{1,3}, 5:{6,7,8}, 6:{5,7}, 7:{5,6,8}, 8:{5,7}, 9:{10,11}, 10:{9,11}, 11:{9,10}, 12:{13,16}, 13:{12,14}, 14:{13,15}, 15:{14,16}, 16:{12,15}, 17:{18,22}, 18:{17,19}, 19:{18,20}, 20:{19,21}, 21:{20,22}, 22:{21,17}, 23:{24}, 24:{23}}
    grafo24 = {1:{2,4}, 2:{1,3}, 3:{2,4}, 4:{1,3}, 5:{6,7,8}, 6:{5,7}, 7:{5,6,8}, 8:{5,7}, 9:{10,11,12}, 10:{9,11,12}, 11:{9,10,12}, 12:{9,10,11}, 13:{14,16,17}, 14:{13,15,16}, 15:{14,16,17,19}, 16:{13,14,15,18}, 17:{13,15}, 18:{16,19}, 19:{15,18}, 20:{20}}
    grafos = [grafo21, grafo22, grafo23, grafo24]
    count = 20
    for grafo in grafos:
        count+=1 
        grafo_dict = grafo
        grafo = Grafo(grafo_to_arestas(grafo))
        MA = grafo_to_matriz(grafo)
        criar_arquivo_grafo("ex"+str(count), grafo, MA)
        imprimir_matriz(MA)

        imprime_calcula_componentes_e_media(grafo_dict)
        
def main(argv):
    init()
    while True:
        option = menu().lower()
        if option == "1":
            file_name = input("Digite o nome do grafo:")
            try:
                arquivo = carrega_arquivo(file_name)
                estrutura = ast.literal_eval(arquivo['estrutura'])
                MA = arquivo['matriz']
                grafo = Grafo(grafo_to_arestas(estrutura)) 
                imprimir_matriz(MA)
            except:
                print("ERRO: Problema ao carregar o arquivo!")

        elif option == "2":
            MA = criar_grafo()
            imprimir_matriz(MA)

        elif option == "3":
            file_name = input("Digite o nome do grafo:")
            try:
                arquivo = carrega_arquivo(file_name)
                estrutura = ast.literal_eval(arquivo['estrutura'])
                MA = arquivo['matriz']
                imprime_calcula_componentes_e_media(estrutura)
            except:
                print("ERRO: Problema ao carregar o arquivo!")
        elif option == "4":
            #Gerar matriz de adjacência do grafo de Micielski
            while True:
                w = int(input("Digite o número da clique do grafo de Micielski."))   
                x = int(input("Digite o número cromático do grafo de Micielski."))
                if (w>=2):
                    if (x>=w):
                            imprimir_matriz(matriz_grafo_mycielsky(x,w))
                            break
                    else:
                        print("O valor da clique precisa ser menor ou igual ao número cromático.")
                else:
                        print("O valor da clique precisa ser maior ou igual a 2.")
                
        elif option == "5":
            file_name = input("Digite o nome do grafo:")
            try:
                arquivo = carrega_arquivo(file_name)
                estrutura = ast.literal_eval(arquivo['estrutura'])
                grafo = Grafo(grafo_to_arestas(estrutura))
                print("vetor coloração: ",get_coloracao(grafo))
            except:
                print("ERRO: Problema ao carregar o arquivo!")

        elif option == "6":
            try:
                file_name = input("Digite o nome do grafo:")
                arquivo = carrega_arquivo(file_name)
                estrutura = ast.literal_eval(arquivo['estrutura'])
                grafo = Grafo(grafo_to_arestas(estrutura))
                is_euleriano(grafo, file_name)
            except:
                print("ERRO: Problema ao carregar o arquivo!")
            
            
            
        elif option == 's':
            break
        if(input("Se deseja sair pressione s ou pressione qualquer outra tecla para continuar.").lower()=='s'):
            break



if __name__ == "__main__":
   main(sys.argv[1:])   