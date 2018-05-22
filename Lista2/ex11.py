# -*- coding: cp1252 -*-
'''
O programa lê uma frase com várias palavras e exibe a primeira palavra invertida.

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

def inverte(str1):
    str1_inv = ''
    for i in range(len(str1)):
        str1_inv += str1[(len(str1)-1)-i] 
    return str(str1_inv)

def impr(palavra_inv):
    print 'Primeira palavra invertida é: {:1s}.'.format(palavra_inv)
    return

frase = ler()
palavras = separa_palavras(frase)
palavra_inv = inverte(palavras[0])
impr(palavra_inv)
