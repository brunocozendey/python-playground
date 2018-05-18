# -*- coding: cp1252 -*-
'''
Programa lê 2 strings e informa o conteúdo delas seguido do seu comprimento.
Informa também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes
no conteúdo.(considerando que letras maiúsculas e minúsculas são iguais).
O programa deverá ser modularizado com pelo menos 2 funções
Todas as respostas devem vir com mensagens explicativas.

Criado por: Bruno Cozendey
Criado em: 17/05/2018

'''

def ler():
    while True:
        try:    
            str1 = str(raw_input('Entre com a primeira string: \n'))
            str2 = str(raw_input('Entre com a segunda string: \n'))
            break
        except:
            print 'Ooops algo ocorreu de errado!'
    return str1,str2

def conta_str(str1,str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if str1_len == str2_len:
        len_compare = 'As duas strings possuem o mesmo comprimento'
    else:
        len_compare = 'As duas strings não possuem o mesmo comprimento'
    return str1_len, str2_len,len_compare

def compara_str(str1,str2):
    if (str1.lower() == str2.lower()):
        status_compare = 'As strings são iguais!'
    else:
        status_compare = 'As strings não são iguais!'
    return status_compare
         


def exib(str1,str2,str1_len,str2_len,len_compare,status_compare):
    print '-----------------------------------'
    print 'Primeira String: '+str1
    print 'Comprimento da primeira string:',str1_len
    print 'Segunda String: '+str2
    print 'Comprimento da segunda string:',str2_len
    print len_compare
    print status_compare
    

#Main
str1,str2 = ler()
str1_len,str2_len,len_compare = conta_str(str1,str2)
status_compare = compara_str(str1,str2)
exib(str1,str2,str1_len,str2_len,len_compare,status_compare)

