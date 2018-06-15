# -*- coding: cp1252 -*-
'''
O programa lê uma matriz de mxn valores reais.
Classifica e exibe a primeira linha em ordem crescente usando Bubble Sort.

Criado por: Bruno Cozendey
Em: 31/05/2018
'''
def ler():
    m = 0
    n = 0
    while True:
        try:    
            m = int(raw_input('Matriz com quantas linhas:'))
            if m > 1:                      
                break
            else:
                raise
        except:
            print 'Precisa ser um número inteiro e maior que 0'
        
    while True:    
        try:    
            n = int(raw_input('Matriz com quantas colunas:'))
            if n > 0:                      
                break
            else:
                raise
        except:
            print 'Precisa ser um número inteiro e maior que 0'
    a = m*[None]
    for i in range(m):
        a[i] = n*[None]    
        for j in range(n):
            while True:    
                try:    
                    a[i][j] = float(raw_input('A['+str(i+1)+']['+str(j+1)+'] = '))
                    break
                except:
                    print 'Precisa ser um número real'        
    
    return a

def bubbleSort(a):
    linha = a[0]
    troca = True
    while troca == True:
        troca = False
        for i in range(len(linha)-1):
            if linha[i] > linha[i+1]:
                linha[i],linha[i+1] = linha[i+1],linha[i]
                troca = True
    return linha 

def impr(linha):
    print linha  

#MAIN
a = ler()
linha = bubbleSort(a)
impr(linha)
