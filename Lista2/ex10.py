# -*- coding: cp1252 -*-
'''
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), o programa conta:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais (independentemente se são maiúsculas ou minúsculas)

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

def conta_esp(frase):
    n_esp = 0
    letra = ''
    for letra in frase:
        if letra == ' ':
            n_esp += 1
    return n_esp

def vogais(frase):
    n_vogais = 0
    for i in frase:
        if i.lower() in ['a','e','i','o','u']:
            n_vogais +=1
    return n_vogais

def impr(frase,n_vogais,n_esp):
    print 'A frase: {:1s}.\nPossui: {:1,d} vogais e {:1,d} espaços em branco.'.format(frase,n_vogais,n_esp)
    return


frase = ler()
n_esp = conta_esp(frase)
n_vogais = vogais(frase)
impr(frase,n_vogais,n_esp)
