# -*- coding: cp1252 -*-
'''
o programa lê uma frase (string) conta e exibe o número de palavras dessa frase.
Considera que as palavras podem ser separadas por espaços brancos ou vírgulas. 
Exemplos: 
contém 1 palavra. ‘Processamento da informação’ contém 3 palavras. ‘computador, caderno e caneta’
contém 4 palavras. ‘ linux ’ contém 1 palavra. ‘ ’ não contém palavras. ‘ , , , ’ não contém palavras. O

Criado por: Bruno Cozendey
Em: 25/05/2018
'''
def ler():
    try:
        frase = raw_input('Escreve uma frase: ')
    except:
        print 'Oops algo deu errado!'
    return frase

def separa(frase):
    f_separada = frase.split(' ')
    f_final = []
    for i in range(len(f_separada)):
        palavra = ''
        for j in f_separada[i]:
            if j.lower() in ['a','á','à','ã','b','c','ç','d','e','é','ê','f','g','h','i','í','j','k','l','m','n','o','ó','ô','p','q','r','s','t','u','ú','w','v','x','y','z']:
                palavra += j
        if palavra !='': #Necessário para o caso de espaço ou o que não estiver na lista acima de letras (outros caracteres)
            f_final.append(palavra)
    return len(f_final)

def impr(n_palavras):
    if n_palavras == 1:
        quantidade = 'contém 1 palavra'
    elif n_palavras > 1:
        quantidade = 'contém {:1d} palavras'.format(n_palavras)
    else:
        quantidade = 'não contém palavras.'
    print 'Sua frase {:1s}'.format(quantidade)

#MAIN
frase = ler()
n_palavras = separa(frase)
impr(n_palavras)
