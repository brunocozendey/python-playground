# -*- coding: cp1252 -*-
'''
O programa conta a quantidade de vogais e de consoantes de uma string. 
O usuário pode usar letras maiúsculas e/ou minúsculas
Criado por: Bruno Cozendey
Em: 19/05/2018
'''
def ler():
    while True:
        try:    
            frase = raw_input('Digite uma palavra: \n')
            break
        except:
            print 'Oops saiu algo errado!'
    return frase

def vogais(frase):
    n_vogais = 0
    for i in frase:
        if i.lower() in ['a','e','i','o','u']:
            n_vogais +=1
    return n_vogais

def consoantes(frase):
    n_consoantes = 0
    for i in frase:
        if i.lower() in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            n_consoantes +=1
    return n_consoantes

def impr(frase,n_vogais,n_consoantes):
    print 'A sua string é \'{:1s}\', possui {:d} vogais e {:d} consoantes.'.format(frase,n_vogais,n_consoantes)

#Main
frase = ler()
n_vogais = vogais(frase)
n_consoantes = consoantes(frase)
impr(frase, n_vogais,n_consoantes)
