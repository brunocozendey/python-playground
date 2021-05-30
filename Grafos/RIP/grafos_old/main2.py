#!/usr/bin/python
import sys, getopt,json
import numpy as np
from Grafo import Grafo
import ast

barra = "="*30

grafo = {
    	1 : [2, 4],
    	2 : [1, 3],
    	3 : [2, 4],
    	4 : [1, 3]
	    }

def menu():
    print(barra)
    print("|       IMPRIME GRAFOS       |")
    print(barra)
    print(barra)
    print("Digite a opção desejada")
    print("1. Carregar grafo existente")
    print("2. Criar um novo grafo")
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

def grafo_to_arestas(g):
    arestas = []
    for vertice in grafo:
        for vertice_aresta in grafo[vertice]:
            arestas.append((vertice,vertice_aresta))    
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
    estrutura = matriz_to_grafo(MA).adj

    criar_arquivo_grafo(nome_grafo,estrutura, MA)

    return MA


def init():
    grafo1 = "0,1,0,1;1,0,1,0;0,1,0,1;1,0,1,0"
    MA1 = str_to_matriz(grafo1)
    criar_arquivo_grafo("grafo1",MA1)
    MA1 = carrega_matriz_arquivo("grafo1")
    imprimir_matriz(MA1)

def main(argv):
    #init()
    while True:
        option = menu().lower()
        if option == "1":
            file_name = input("Digite o nome do grafo:")
            arquivo = carrega_arquivo(file_name)
            MA = arquivo['matriz']
            grafo = Grafo(grafo_to_arestas(arquivo['estrutura'])) 
            imprimir_matriz(MA)
        elif option == "2":
            MA = criar_grafo()
            imprimir_matriz(MA)
        elif option == 's':
            break   

if __name__ == "__main__":
   main(sys.argv[1:])   