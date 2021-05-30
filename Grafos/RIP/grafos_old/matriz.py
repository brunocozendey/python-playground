#!/usr/bin/python
import json
import sys, getopt
import numpy as np
from Grafo import Grafo
import ast

def criar_matriz_zeros(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha) 
    return matriz

def grafo_to_matriz(g):
    arestas = grafo_to_arestas(g)        
    M = criar_matriz_zeros(len(g))
    for va,vb in arestas:
        M[va-1][vb-1] = 1
    return M



def grafo_to_arestas(g):
    arestas = []
    for vertice in grafo:
        for vertice_aresta in grafo[vertice]:
            arestas.append((vertice,vertice_aresta))    
    return arestas

def matriz_to_grafo(M):
    arestas = []
    for linha in range(len(M)):
        for coluna in range(len(M)):
            if M[linha][coluna] == 1:
                arestas.append((linha+1,coluna+1))
    g = Grafo(arestas)
    return g



grafo = {
    	1 : [2, 4],
    	2 : [1, 3],
    	3 : [2, 4],
    	4 : [1, 3]
	    }


grafo_file = open("grafos/ex3.txt", "r", encoding='utf-8')
grafo_file.seek(0)
#file_data = grafo_file.read()
grafo_json = json.load(grafo_file)
M = grafo_json['matriz']


#print(grafo_json['matriz'])

#M = grafo_to_matriz(grafo)
print(matriz_to_grafo(M))
print(json.dumps(str(matriz_to_grafo(M))))

#print(grafo)
