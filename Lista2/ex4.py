# -*- coding: cp1252 -*-
'''
Este programa solicita a data de nascimento (dd/mm/aaaa) do usuário e imprime a data
com o nome do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.

Criado por: Bruno Cozendey
Criado em: 17/05/2018
'''

def ler():
    while True:
        try:    
            data = str(raw_input('Digite sua data de nascimento (dd/mm/aaaa): \n'))
            dia = int(data[0:2])
            mes = int(data[3:5])
            ano = int(data[6:])
            if data[2] == '/' and data[5] == '/' and len(data) == 10 and dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano >1918 and ano <= 2018:
                break
            else:
                reise
        except:
            print 'O formato da data deve ser (dd/mm/aaaa)'
    return dia, mes, ano

def extenso(dia,mes,ano):
    if mes == 1:
        mes_ext = 'Janeiro'
    elif mes == 2:
        mes_ext = 'Fevereiro'
    elif mes == 3:
        mes_ext = 'Março'
    elif mes == 4:
        mes_ext = 'Abril'
    elif mes == 5:
        mes_ext = 'Maio'
    elif mes == 6:
        mes_ext = 'Junho'
    elif mes == 7:
        mes_ext = 'Julho'
    elif mes == 8:
        mes_ext = 'Agosto'
    elif mes == 9:
        mes_ext = 'Setembro'
    elif mes == 10:
        mes_ext = 'Outubro'
    elif mes == 11:
        mes_ext = 'Novembro'    
    elif mes == 12:
        mes_ext = 'Dezembro'
    print 'Você nasceu em',dia,'de',mes_ext,'de',ano,'.'

#Main
dia, mes, ano = ler()
extenso(dia,mes,ano)
