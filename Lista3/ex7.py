# -*- coding: cp1252 -*-
'''
O programa intercalar os elementos de duas listas de
igual comprimento. Exemplo: [’a’,10,’b’,20,’c’,30,’d’,40] é o resultado de intercalar as listas:
L1=[’a’,’b’,’c’,’d’] e L2= [10,20,30,40].

Criado por: Bruno Cozendey
Em: 14/06/2018
''' 

def ler():
    lista1 = []
    lista2 = []
    while True:
        try:    
            l1 = raw_input('Digite o item da Lista 1:')
            if l1.isalpha():                      
                lista1.append(l1)
                try:    
                    l2 = int(raw_input('Digite o item da Lista 2:'))
                    lista2.append(l2)
                except:
                    print 'Precisa ser número'
            elif l1 == '':
                break
            else:
                raise
        except:
            print 'Precisa ser letra'
    return lista1,lista2

def concat(lista1,lista2):
    listaf = []
    for i in range(len(lista1)):
        listaf.append(lista1[i])
        listaf.append(lista2[i])
    return listaf

def impr(listaf):
    print listaf
    return   

#MAIN
lista1,lista2 = ler()
listaf = concat(lista1,lista2)
impr(listaf)
