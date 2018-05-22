# -*- coding: cp1252 -*-
'''
O programa lê uma frase e exiba quantas vogais existem na primeira palavra.

Criado por: Bruno Cozendey
Em: 22/05/2018
'''

def ler():
    while True:
        try:    
            frase = raw_input('Digite uma frase:')
            break
        except:
            print 'Oops saiu algo errado!'
    return frase

def separa_palavras(frase):
    palavra=''
    palavras = []
    for i in range(len(frase)):
        letra = frase[i]
        if letra != ' ':
            palavra +=letra
        else:
            palavras.append(palavra)
            palavra = ''
            ultimo_esp = i
    palavras.append(frase[ultimo_esp+1:])
    return palavras

def vogais(frase):
    n_vogais = 0
    for i in frase:
        if i.lower() in ['a','e','i','o','u']:
            n_vogais +=1
    return n_vogais

def impr(ultima_palavra,n_vogais):
    print 'A Primeira palavra foi: {:1s}.\nPossui: {:1,d} vogais.'.format(ultima_palavra,n_vogais)
    return


frase = ler()
palavras = separa_palavras(frase)
n_vogais = vogais(palavras[0])
impr(palavras[0],n_vogais)
