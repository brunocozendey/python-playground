# -*- coding: cp1252 -*-
'''

Programa lê uma quantidade indeterminada de nomes e exibe quantas vezes o nome
joão aparece independente de sua posição no nome.

Criado por: Bruno Cozendey
Em: 22/05/2018

'''

def ler():
    lista_nomes =[]
    while True:
        try:    
            nome = raw_input('Digite um nome ou [fim] para finalizar a lista:')
            if nome =='fim':
                break
            else:
                lista_nomes.append(nome)
        except:
                print 'Oops saiu algo errado!'    
    return lista_nomes

def isJoao(lista_nomes):
    quantidade = 0
    for nome in lista_nomes:
        if ('João' in nome) or ('joão' in nome):
            quantidade +=1
    return quantidade

def impr(quantidade):
    print 'João aparece {:1d} vezes na sua lista.'.format(quantidade)
    return

lista_nomes = ler()
quantidade = isJoao(lista_nomes)
impr(quantidade)
   
