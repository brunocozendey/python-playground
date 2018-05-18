# -*- coding: cp1252 -*-
'''
Este programa permite o usuário digitar o seu nome e em seguida exibe o nome do
usuário de trás para frente utilizando somente letras maiúsculas. 

Criado por: Bruno Cozendey
Criado em: 17/05/2018

'''

def ler():
    while True:
        try:    
            str1 = str(raw_input('Digite seu nome: \n'))
            break
        except:
            print 'Ooops algo ocorreu de errado!'
    return str1

def inverte(str1):
    str1_inv = ''
    for i in range(len(str1)):
        str1_inv += str1[(len(str1)-1)-i] 
    print 'Seu nome invertido é',str(str1_inv).upper()

#Main
str1 = ler()
str1_inv = inverte(str1)
