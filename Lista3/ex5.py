# -*- coding: cp1252 -*-
'''
O programa lê uma matriz de mxn elementos reais. Determinar o vetor soma da 1ª. Linha com a 2ª. Linha.
Exibe a matriz lida sob a forma de tabela e o vetor soma com 2 casas decimais.

Criado por: Bruno Cozendey
Em: 14/06/2018
''' 

def ler():
    m = 0
    n = 0
    while True:
        try:    
            m = int(raw_input('Matriz com quantas linhas:'))
            if m > 1:                      
                break
            else:
                raise
        except:
            print 'Precisa ser um número inteiro e maior que 0'
        
    while True:    
        try:    
            n = int(raw_input('Matriz com quantas colunas:'))
            if n > 0:                      
                break
            else:
                raise
        except:
            print 'Precisa ser um número inteiro e maior que 0'
    a = m*[None]
    for i in range(m):
        a[i] = n*[None]    
        for j in range(n):
            while True:    
                try:    
                    a[i][j] = float(raw_input('A['+str(i+1)+']['+str(j+1)+'] = '))
                    break
                except:
                    print 'Precisa ser um número real'        
    
    return a,m,n
def soma(a,n):
    s = n*[None]
    for j in range(n):
        s[j] = a[0][j]+a[1][j]
    return s
def impr(a,m,n,s):
    print '\n{:*^20}\n'.format('Matriz Lida')
    for i in range(m):
        for j in range(n):
            print '{:^10.2f}'.format(a[i][j]),
        print '\n'
    print '\n{:*^20}\n'.format('Vetor Soma:')
    for k in range(n):
        print '{:^10.2f}'.format(s[k]),    
    return   

#MAIN
a,m,n = ler()
s = soma(a,n)
impr(a,m,n,s)
