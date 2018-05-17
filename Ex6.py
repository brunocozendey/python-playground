# -*- coding: cp1252 -*-
teste = 2
divisor = 0
while True:
	try:
		num = int(raw_input("Escreva um numero: "))
	except:
        	print "Oops algo errado!"
    	while teste < num:
        	if num%teste == 0:
       			divisor += 1
        	teste += 1 
    	break
if divisor == 0 or num == 1 or num == 2:
    print 'O numero '+str(num)+' e primo!'

