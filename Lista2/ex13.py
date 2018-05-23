# -*- coding: cp1252 -*-
'''
O programa lê o nome e a idade de um grupo indeterminado de pessoas e determina o
maior nome do grupo e a media das idades.

Criado por: Bruno Cozendey
Em: 22/05/2018
'''

def ler():
    lista_nomes= []
    lista_idades=[]
    while True:
        try:    
            nome = raw_input('Digite um nome ou tecle \'Enter\' para finalizar a lista:')
            if nome =='':
                break
            else:
                lista_nomes.append(nome)
        except:
                print 'Oops saiu algo errado!'
        try:    
            idade = float(raw_input('Digite a idade de {:1s}:'.format(nome)))
            lista_idades.append(idade)
        except:
                print 'Oops saiu algo errado!'    
    return lista_nomes, lista_idades

def maiorNome(lista_nomes):
    maior = '' 
    nomes = ''
    for nomes in lista_nomes:
        if (len(str(nomes)) > len(maior)):
            maior = nomes
    return maior

def mediaIdade(lista_idades):
    soma = 0
    media = 0
    n = len(lista_idades)
    for idade in lista_idades:
        i = idade
        soma += i
    media = soma/n
    return media

def impr(maior,media):
    print 'O maior nome é {:1s}, e a média das idades é: {:1.1f}.'.format(maior,media)
    return

lista_nomes,lista_idades = ler()
maior = maiorNome(lista_nomes)
media = mediaIdade(lista_idades)
impr(maior,media)   
