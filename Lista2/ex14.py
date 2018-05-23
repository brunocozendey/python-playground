# -*- coding: cp1252 -*-

'''
O programa lê uma frase com várias palavras e exibe a última palavra
invertida.

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
    palavras=frase.split(' ')
    p_palavra = palavras[len(palavras)-1]
    return p_palavra

def inverte(str1):
    str1_inv = ''
    t_str1 = len(str1) 
    for i in range(t_str1):
        str1_inv += str1[(t_str1-1)-i] 
    return str(str1_inv)

def impr(palavra_inv):
    print 'A útlima palavra invertida é: {:1s}.'.format(palavra_inv)
    return

frase = ler()
p_palavras = separa_palavras(frase)
palavra_inv = inverte(p_palavras)
impr(palavra_inv)
