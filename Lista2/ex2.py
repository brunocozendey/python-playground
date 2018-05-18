# -*- coding: cp1252 -*-
'''
O programa lê uma string (com várias palavras) e verifique se ela é um
palíndromo. Um palíndromo é uma cadeia que pode ser lida de trás para frente ou frente para
trás e possui exatamente o mesmo valor. Exemplo: SUBI NO ONIBUS

Criado por: Bruno Cozendey
Criado em: 17/05/2018

'''

def ler():
    while True:
        try:    
            str1 = str(raw_input('Digite uma frase para verificar se é um palíndromo: \n'))
            break
        except:
            print 'Ooops algo ocorreu de errado!'
    return str1.replace(' ','')

def inverte(str1):
    str1_inv = ''
    for i in range(len(str1)):
        str1_inv += str1[(len(str1)-1)-i] 
    return str(str1_inv)

def compara(str1,str1_inv):
    if str1.lower() == str1_inv.lower():
        print 'É um palíndromo!'
    else:
        print 'Não é palíndromo!'

#Main
str1 = ler()
str1_inv = inverte(str1)
compara(str1,str1_inv)
