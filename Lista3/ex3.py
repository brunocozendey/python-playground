# -*- coding: cp1252 -*-
'''
O programa exibe uma lista com uma quantidade indeterminada de nomes.

Classifica e exibe em ordem alfabética decrescente (x→a)

usando Bubble Sort.

Criado por: Bruno Cozendey
Em: 02/06/2018
''' 

def ler():
    nomes = []
    while True:
        while True:    
            try:    
                nome = raw_input('Digite um nome:')
                nomecheck = nome.split()
                nomecheck = ''.join(nomecheck)
                if nomecheck.isalpha() or nomecheck =='':                      
                    break
                else:
                    raise
            except:
                print 'Usar apenas caracteres válidos'
        if nome == '':
            break
        else:
            nomes.append(nome)

    return nomes

def ordena(nomes):
    troca = True
    while troca == True:
        troca = False
        for i in range(len(nomes)-1):
            if nomes[i].lower() < nomes[i+1].lower():
                nomes[i],nomes[i+1] = nomes[i+1],nomes[i]
                troca = True
    return nomes
def impr(nomes):
    for i in nomes:
            print i     

#MAIN
nomes = ler()
nomes = ordena(nomes)
impr(nomes)
