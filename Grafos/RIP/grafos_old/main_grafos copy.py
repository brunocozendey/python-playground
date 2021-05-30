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


def criar_arquivo_grafo(file_name, matriz):
    while True:
        try:
            grafo_file = open("grafos/"+file_name+'.txt', "w", encoding='utf-8')
            grafo_file.seek(0)
            grafo_file.write(matriz_to_str(matriz))
            grafo_file.close()
            break
        except:
            raise FileNotFoundError('Erro ao criar o arquivo!')
        finally:
            grafo_file.close()

def str_to_matriz(matriz):
    return np.matrix(matriz).tolist()

def carrega_matriz_arquivo(file_name): 
    try:
        grafo_file = open("grafos/"+file_name+'.txt', "r", encoding='utf-8')
        grafo_file.seek(0)
        adjacency_matrix = grafo_file.read()
        
        return str_to_matriz(adjacency_matrix)
        #print(adjacency_matrix)  
        #grafo_json = ast.literal_eval(grafo_str)
        #grafo = Grafo([("a","b"), ( "b", "c"), ("c","d"), ("d","a")]) 
        #print(grafo)
        #print(ast.literal_eval(grafo_str)) 

    except:
        raise FileNotFoundError('Arquivo de Grafo não encontrado!')
    finally:
        grafo_file.close()

def criar_grafo():
    nome_grafo = input("Digite o nome do grafo: ")
    while True:
        try:
            numero_arestas = int(input("Indique um número de arestas (Valor inteiro): "))
            break
        except ValueError:
            print('O valor precisa ser um inteiro.')
    MA = espelhar_matriz(cria_matriz_adjacencia(numero_arestas))
    criar_arquivo_grafo(nome_grafo,MA)
    return MA


def init():
    grafo1 = "0,1,0,1;1,0,1,0;0,1,0,1;1,0,1,0"
    MA1 = str_to_matriz(grafo1)
    criar_arquivo_grafo("grafo1",MA1)
    MA1 = carrega_matriz_arquivo("grafo1")
    imprimir_matriz(MA1)

def main(argv):
    init()
    while True:
        option = menu().lower()
        if option == "1":
            file_name = input("Digite o nome do grafo:")
            MA = carrega_matriz_arquivo(file_name)
            imprimir_matriz(MA)
        elif option == "2":
            MA = criar_grafo()
            imprimir_matriz(MA)
        elif option == 's':
            break   

if __name__ == "__main__":
   main(sys.argv[1:])   