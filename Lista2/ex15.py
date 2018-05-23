# -*- coding: cp1252 -*-

'''
O programa que lê um número de telefone, e corrije o número no caso deste conter somente 7
dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
No final o programa exibe o numero do telefone formatado.
Exemplo:
Input: 461-0133
Output: 3461-0133

Criado por: Bruno Cozendey
Em: 22/05/2018
'''

def ler():
    while True:
        try:    
            tel = raw_input('Digite um telefone:')
            for i in tel:    
                if i not in ['0','1','2','3','4','5','6','7','8','9','-'] or len(tel) < 7 or len(tel) > 8:
                    reise
            break
        except:
            print 'Só são aceitos números e o traço separador \'-\' para o telefone e precisa ter no mínimo 7 dígitos e no máximo 8!'
    return tel

def check(tel):
    tel_num = ''
    for i in tel:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            tel_num += i
    if len(tel_num) < 8:
        tel_num = '3'+tel_num
    tel_form = tel_num[0:4]+'-'+tel_num[4:8]
    return tel_form
    
def impr(tel_form):
    print 'O telefone formatado é: {:1s}.'.format(tel_form)
    return

tel = ler()
tel_form = check(tel)
impr(tel_form)
