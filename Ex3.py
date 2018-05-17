# -*- coding: cp1252 -*-
preco_maior = 0
produto_caro =''
while True:
	produto = raw_input("Escreva o nome do produto?")
	if produto == 'XXX':
        	break
    	try:
        	preco = float(raw_input('Escreva o preco do produto '+produto+' ?'))
        	if preco_maior < preco:
            		preco_maior = preco
            		produto_caro = produto
	except:
	        print "Oops algo errado!"
print 'Produto mais caro e: '+produto_caro
