# -*- coding: cp1252 -*-
'''
Este programa lê uma frase com várias palavras e exibe a primeira e a última
palavra ao final.

Criado por: Bruno Cozendey
Em: 20/05/2018
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

def impr(palavras):
    print 'Primeira palavra foi: {:1s}.\nA última palavra foi: {:1s}.'.format(palavras[0],palavras[len(palavras)-1])
    return

frase = ler()
palavras = separa_palavras(frase)
impr(palavras)
