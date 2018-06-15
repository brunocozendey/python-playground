# -*- coding: cp1252 -*-
'''
O programa lê uma matriz quadrada de m elementos reais. 
Determina a soma dos termos da diagonal principal menos a soma dos termos de diagonal secundária.
Exibe o resultado com duas casas decimais.

Criado por: Bruno Cozendey
Em: 14/06/2018
''' 

def ler():
    m = 0
    while True:
        try:    
            m = int(raw_input('Matriz quadrada com quantas linhas e colunas:'))
            if m > 1:                      
                break
            else:
                raise
        except:
            print 'Precisa ser um número inteiro e maior que 0'
        
    a = m*[None]
    for i in range(m):
        a[i] = m*[None]    
        for j in range(m):
            while True:    
                try:    
                    a[i][j] = float(raw_input('A['+str(i+1)+']['+str(j+1)+'] = '))
                    break
                except:
                    print 'Precisa ser um número real'        
    
    return a,m
def soma(a,m):
    sp = 0
    ss = 0
    for j in range(m):
        sp += a[j][j]
        ss += a[m-1-j][j]
        total = sp - ss   
    return total

def impr(a,m,total):
    print '\n{:*^20}\n'.format('Matriz Lida')
    for i in range(m):
        for j in range(m):
            print '{:^10.2f}'.format(a[i][j]),
        print '\n'
    print '\n{:*^20}\n'.format('Soma da diagonal principal menos diagonal secundária:')
    print '{:.2f}'.format(total)
    return   

#MAIN
a,m = ler()
total = soma(a,m)
impr(a,m,total)
