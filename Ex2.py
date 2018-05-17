# -*- coding: cp1252 -*-
par = impar = total_par = 0
while True:
    try:
	    num = int(raw_input("Escreva um numero?"))
	    if num == 0:
		break
	    if (num%2 == 0):
		par+=1
		total_par += num
	    else:
		impar+=1
    except:
        print 'Oops algo errado!'

print 'Quantidade de numeros pares: '+str(par)
print 'Quantidade de numeros impares: '+str(impar)
if total_par == 0:
    print 'A media de numeros pares: 0'
else:
    print 'A media de numeros pares: '+str(total_par/float(par))