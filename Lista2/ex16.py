# -*- coding: cp1252 -*-
'''
Este faz 5 perguntas para o usuário e ao final emite uma classificação
de acordo com a quantidade de respostas s ou n que o usuário forneceu.

Criado por: Bruno Cozendey
Em: 23/05/2018
'''

def ler(perguntas):
    respostas= []
    for p in perguntas:
        while True:
            try:
                r = raw_input(p)
                r = r.lower()
                if r not in ['s','n']:
                    reise
                respostas.append(r)
                break
            except:
                print 'Responda apenas s ou n!'
    return respostas

def check(repostas):
    total_s = 0
    for r in respostas:
        if r == 's':
            total_s+=1
    if total_s == 2:
        status = 'Suspeita'
    elif total_s == 3 or total_s == 4:
        status = 'Cúmplice'
    elif total_s == 5:
        status = 'Assassino'
    else:
        status = 'Inocente'

    return status
    
def impr(status):
    print 'Você é: {:1s}.'.format(status)
    return

#Main
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
respostas = ler(perguntas)
status = check(respostas)
impr(status)
