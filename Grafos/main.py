#!/usr/bin/python
#lista_compras = [itens, quantidade, preço(und,peso,pct)]

# Testar com lista vazia, quantidade float e inteiro, preço float e inteiro.
lista_mercado = [
    {
    'item':'banana',
    'quantidade': 2,
    'preço': 2.00,
    },
    {
    'item':'maçã',
    'quantidade': 5,
    'preço': 9.89,
    },
    {
    'item':'Laranja',
    'quantidade': 1.670,
    'preço': 7.99,
    },
    {
    'item':'pão',
    'quantidade': 2,
    'preço': 5.99,
    },
    {
    'item':'queijo',
    'quantidade': 0.100,
    'preço': 59.90,
    }
]

# Testar lista de pessoas com 0, 1 , 2, 3, 7, 100, 101, 1001
lista_pessoas = [
    'teste1@gmail.com', 
    'teste2@gmail.com', 
    'teste3@gmail.com', 
    'teste4@gmail.com',
    'teste5@gmail.com',
    'teste6@gmail.com',
    'teste7@gmail.com' 
]

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
    print("A diferença foi de {} e o os diferentes são: {}".format(valor_por_um_centavo-valor_total_dividido, quantidade_valores_diferentes))

    if valor_total_dividido != valor_total:
        return valor_por_pessoa/100, (valor_por_pessoa+1)/100, quantidade_valores_diferentes
    else:
        return valor_por_pessoa/100, valor_por_pessoa/100, 0

def distribuir_valor_por_email(lista_emails):
    lista_email_com_valor = {}
    valor_normal, valor_arredondado, quantidade_valores_diferentes = dividir_igualmente(calcula_valor_total(lista_mercado),len(set(lista_emails)))
    for email in lista_emails:
        lista_email_com_valor[email]=valor_normal
    for i in range(quantidade_valores_diferentes):
        lista_email_com_valor[lista_emails[i]] = valor_arredondado
    return lista_email_com_valor



print (calcula_valor_total(lista_mercado))
print(dividir_igualmente(calcula_valor_total(lista_mercado),6))
print(distribuir_valor_por_email(lista_pessoas))
{'teste1@gmail.com': 14.13, 'teste2@gmail.com': 14.12, 'teste3@gmail.com': 14.12, 'teste4@gmail.com': 14.12, 'teste5@gmail.com': 14.12, 'teste6@gmail.com': 14.12}

{'teste1@gmail.com': 12.11, 'teste2@gmail.com': 12.11, 'teste3@gmail.com': 12.11, 'teste4@gmail.com': 12.11, 'teste5@gmail.com': 12.11, 'teste6@gmail.com': 12.11, 'teste7@gmail.com': 12.1}