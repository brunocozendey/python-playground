# -*- coding: cp1252 -*-
'''Programa que lê 2 vetores de tamanho N e exibe o vetor soma dos dois'''
def ler():
    vetor_a = vetor_b = []
    while True:
        try:    
            n = int(raw_input('Qual o tamanho dos vetores:'))
            break
        except:
            print 'Opção inválida'

    for i in range(n):
	while True:
            try:        
	        a = int(raw_input('Diga o elemento da posição '+str(i)+ ' do vetor a: '))
                break
            except:
                print 'Opção inválida'
	while True:
            try:  
                b = int(raw_input('Diga o elemento da posição '+str(i)+ ' do vetor b: '))
                break
            except:
                print 'Opção inválida'

	vetor_soma.append(a+b)
    return vetor_soma

def exib(vetor_soma):
    print 'Vetor soma = ' + str(vetor_soma)

#Main
vetor_soma = []
ler()
exib(vetor_soma)

