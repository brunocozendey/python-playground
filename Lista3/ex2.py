# -*- coding: cp1252 -*-

'''
O programa lê duas listas com uma quantidade indeterminada de valores reais
e de mesmo tamanho e determina e exibe sua soma.

Criado por: Bruno Cozendey
Em: 02/06/2018
''' 
def ler():
    lista1 = []
    lista2 = []
    while True:    
        try:    
            num = float(raw_input('Digite números lista 1:\n'))
            lista1.append(num)
            num = raw_input('Digite números lista 2:\n')
            lista2.append(num)
            res = raw_input('A lista terminou ? [s/n]:')
            if res.lower() == 's':
                break
        except TypeError:
            print 'São aceitos apenas número reais'
        except:
            print 'Oops algo deu errado!'
    return lista1, lista2

def somaLista(lista1,lista2):
    vetor_soma = [None]*len(lista1)
    for i in range(len(lista1)):
        vetor_soma[i] = float(lista1[i]) + float(lista2[i]) 
    return vetor_soma

def impr(vetor_soma):
    for i in vetor_soma:
            print i    

#MAIN
lista1,lista2 = ler()
vetor_soma = somaLista(lista1,lista2)
impr(vetor_soma)
