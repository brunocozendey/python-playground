# -*- coding: cp1252 -*-
'''
O programa cria uma lista com uma
quantidade indeterminada de nomes. Verificar se um nome lido se encontra nesta lista usando
pesquisa binária.

Criado por: Bruno Cozendey
Em: 14/06/2018
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
            if nomes[i].lower() > nomes[i+1].lower():
                nomes[i],nomes[i+1] = nomes[i+1],nomes[i]
                troca = True
    return nomes

def busca(nomes):
    while True:    
            try:    
                nomep = raw_input('Digite um nome para verificar na lista: ')
                nomecheck = nomep.split()
                nomecheck = ''.join(nomecheck)
                if nomecheck.isalpha():                      
                    break
                else:
                    raise
            except:
                print 'Usar apenas caracteres válidos'
    final = len(nomes)-1
    inicial = 0
    status = False
    while True:
        media = inicial+((final - inicial) /2)
        if nomes[media].lower() == nomep.lower():
            status = True
            break
        elif nomes[media].lower() > nomep.lower():
            final = media
        elif final == 1 or inicial == final-2:
            if nomes[len(nomes)-1].lower() == nomep.lower() or nomes[0].lower() == nomep.lower():
                status = True
            break
        else:
            inicial = media
    return status,nomep

def impr(status,nomep):
    if status == True:
        print 'O nome \"{:1s}\" foi ENCONTRADO na lista.'.format(nomep)
    else:
        print 'O nome \"{:1s}\" NÃO foi encontrado na lista.'.format(nomep)
    return
#MAIN
nomes = ler()
nomes = ordena(nomes)
status,nomep = busca(nomes)
impr(status,nomep)

