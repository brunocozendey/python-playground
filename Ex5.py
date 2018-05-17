# -*- coding: cp1252 -*-
soma = num = 0
while True:
	try:
		A = int(raw_input("Escreva um numero inteiro positivo A: "))
	        if A < 0:
	            reise
	except:
        	print "Tem que ser positivo!"
    
    	try:
        	B = int(raw_input("Escreva um numero inteiro positivo B: "))
        	if B<0:
        	    reise
    	except:
        	print "Tem que ser positivo!"
    
    	if A > B:
        	print "A soma nao sera realizada!"
    	num = A + 1
    	while num < B:
            if num%4==0:
                soma += num
		num +=1
    	break
print 'A soma dos numeros entre '+str(A)+' e '+str(B)+' e :'+str(soma)
