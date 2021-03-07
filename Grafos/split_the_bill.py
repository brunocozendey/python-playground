#!/usr/bin/python
import sys, getopt,json
import numpy as np
from Grafo import Grafo
import ast


grafo = { "A" : ["B"],
          "B" : ["C", "D"],
          "C" : ["B", "E"],
          "D" : ["A"],
          "E" : ["B"]
        }

#grafo_str = '{ "A" : ["B"],"B" : ["C", "D"],"C" : ["B", "E"],"D" : ["A"],"E" : ["B"]}'

def menu():
    print("=============================")
    print("|       IMPRIME GRAFOS      |")
    print("=============================")
    print("=============================")
    print("Digite a opção desejada")
    print("1. Carregar grafo existente")
    print("2. Criar um novo grafo")
    print("Ou S/s para sair.")
    option = input("Opção:")
    return option

def imprimir_matriz(M):
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
    imprimir_matriz(M)
    return M



def cria_matriz_adjacencia(n):
    M = criar_matriz_zeros(n)
    print(M)
    for i in range(n):
        for j in range(i,n):
            while True:
                try:
                    M[i][j] = int(input('Digite o valor 0/1 da posiçõa [{}][{}] da matriz adjacência:'.format(i,j)))
                    imprimir_matriz(M)
                    if M[i][j] in [0,1]:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("O valor deve ser 0 ou 1")
    return M




def carrega_grafo():
    file_name = input("Digite o nome do grafo:") 
    try:
        grafo_file = open("grafos/"+file_name+'.txt', "r", encoding='utf-8')
        grafo_file.seek(0)
        grafo_str = grafo_file.read()
        #adjacency_matrix = grafo_file.readline()
        #adjacency_matrix = np.matrix(adjacency_matrix).tolist()
        #print(adjacency_matrix)  
        grafo_json = ast.literal_eval(grafo_str)
        grafo = Grafo([("a","b"), ( "b", "c"), ("c","d"), ("d","a")]) 
        print(grafo)
        print(ast.literal_eval(grafo_str)) 
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
    print(numero_arestas, nome_grafo)
    MA = cria_matriz_adjacencia(numero_arestas)
    return espelhar_matriz(MA)


def main(argv):
    while True:
        option = menu().lower()
        if option == "1":
            print(option)
            carrega_grafo()
        elif option == "2":
            criar_grafo()

        elif option == 's':
            break


    
    

def main2(argv):
    """
    Main function that calculate the total price from a grocery list and split it between the people in list emails.

    Args:
        argv (string): get the arg with file name.

    Raises:
        FileNotFoundError: If not found the list file. 
        FileNotFoundError: If not found the list file.
    """
    groceryfile = ''
    emailfile = ''
    try:
       opts, _ = getopt.getopt(argv,"hgl:el:",["glfile=","elfile="])
    except getopt.GetoptError:
        print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
        print ('Please provide input files or -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
            sys.exit()
        elif opt in ("-gl", "--glfile"):
            groceryfile = arg
        elif opt in ("-el", "--elfile"):
            emailfile = arg
   
    try:
        mf = open(groceryfile, "r", encoding='utf-8')
        mf.seek(0)
        grocery_list = mf.read()
        if grocery_list == '':
            grocery_list = "{}"
        grocery_list_json = json.loads(grocery_list)
    except:
        raise FileNotFoundError('Grocery list not found!')
    finally:
        mf.close()

    try:
        ef = open(emailfile, "r", encoding='utf-8')
        ef.seek(0)
        email_list = ef.read().splitlines()
        if email_list == []:
            email_list = ["Total"]
    except:
        raise FileNotFoundError('Email list not found!')
    finally:
        ef.close()
    print(json.dumps(map_price_and_email(email_list,grocery_list_json)))        

if __name__ == "__main__":
   main(sys.argv[1:])   