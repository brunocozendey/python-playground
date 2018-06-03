# -*- coding: cp1252 -*-
'''
O programa lê uma quantidade indeterminada de datas dd/mm/aaaa. 
Classifica e exibe em ordem ascendente, utilizando um algoritmo bubble sort. 

Criado por: Bruno Cozendey
Em: 31/05/2018
'''
def ler():
    lista_datas = []
    while True:    
        try:    
            data = str(raw_input('Digite sua data de nascimento (dd/mm/aaaa) ou enter para finalizar: \n'))
            dia = data[0:2]
            mes = data[3:5]
            ano = data[6:]
            if data == "":
                break
            elif data[2] == '/' and data[5] == '/' and len(data) == 10 and int(dia) > 0 and int(dia) <= 31 and int(mes) > 0 and int(mes) <= 12 and int(ano) >1500 and int(ano) <= 2018:
                lista_datas.append(data)
            else:
                raise
        except:
            print 'O formato da data deve ser (dd/mm/aaaa)'
    return lista_datas

def bubbleSort(lista_datas):
    for num in range(len(lista_datas)-1,0,-1):
        for i in range(num):
            if (int(lista_datas[i][6:]) > int(lista_datas[i+1][6:])) and (int(lista_datas[i][3:5])>int(lista_datas[i+1][3:5])) and (int(lista_datas[i][0:2])>int(lista_datas[i+1][0:2])):
                temp = lista_datas[i]
                lista_datas[i] = lista_datas[i+1]
                lista_datas[i+1] = temp
    return lista_datas

def impr(lista_datas):
    for i in lista_datas:
            print i    

#MAIN
lista_datas = ler()
lista_datas = bubbleSort(lista_datas)
impr(lista_datas)
