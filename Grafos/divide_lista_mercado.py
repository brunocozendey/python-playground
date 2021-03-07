#!/usr/bin/python

import sys, getopt
import json

def calcula_valor_cada_item(item):
    return item['quantidade']*item['preço']

def calcula_valor_total(lista):
    total = 0
    for item in lista:
        total += calcula_valor_cada_item(item)
    return total

def dividir_igualmente(valor_total,numero_pessoas):
    valor_por_um_centavo = valor_total*100
    valor_por_pessoa = valor_por_um_centavo//numero_pessoas
    valor_total_dividido = valor_por_pessoa*numero_pessoas
    quantidade_valores_diferentes = int(valor_por_um_centavo%numero_pessoas)
    
    if valor_total_dividido != valor_total:
        return valor_por_pessoa/100, (valor_por_pessoa+1)/100, quantidade_valores_diferentes
    else:
        return valor_por_pessoa/100, valor_por_pessoa/100, 0

def distribuir_valor_por_email(lista_emails,lista_mercado):
    lista_email_com_valor = {}
    valor_normal, valor_arredondado, quantidade_valores_diferentes = dividir_igualmente(calcula_valor_total(lista_mercado),len(set(lista_emails)))
    for email in lista_emails:
        lista_email_com_valor[email]=valor_normal
    for i in range(quantidade_valores_diferentes):
        lista_email_com_valor[lista_emails[i]] = valor_arredondado
    return lista_email_com_valor

def main(argv):
    marketfile = ''
    emailfile = ''
    try:
       opts, args = getopt.getopt(argv,"hml:el:",["mlfile=","elfile="])
    except getopt.GetoptError:
        print ('divide_lista_mercado.py --ml <marketlist.txt> --el <emaillist.txt>')
        print ('Please provide input files or -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('divide_lista_mercado.py --ml <marketlist.txt> --el <emaillist.txt>')
            sys.exit()
        elif opt in ("-ml", "--mlfile"):
            marketfile = arg
        elif opt in ("-el", "--elfile"):
            emailfile = arg
   
    try:
        mf = open(marketfile, "r", encoding='utf-8')
        #lista_mercado = mf.readlines()
        lista_mercado = json.load(mf)
    except:
        raise FileNotFoundError('Arquivo da lista de mercado não foi encontrado!')
    finally:
        mf.close()

    try:
        ef = open(emailfile, "r", encoding='utf-8')
        lista_pessoas = ef.read().splitlines()     
    except:
        raise FileNotFoundError('Arquivo da lista de pessoas não foi encontrado!')
    finally:
        ef.close()

    print ('market file is "', marketfile)
    print ('email file is "', emailfile)
    print(distribuir_valor_por_email(lista_pessoas,lista_mercado))
    #print(lista_pessoas, lista_mercado)

if __name__ == "__main__":
   main(sys.argv[1:])   