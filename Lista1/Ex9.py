# -*- coding: cp1252 -*-
import math
delta=area = S = h = 0
try:
    ladoA = int(raw_input("Comprimento lado A do triangulo: "))
    if ladoA <=0:
        reise
except:
    print 'Numero precisa ser maior que zero'
try:
    ladoB = int(raw_input("Comprimento lado B do triangulo: "))
    if ladoB <=0:
        reise
except:
    print 'Numero precisa ser maior que zero'
try:
    ladoC = int(raw_input("Comprimento lado C do triangulo: "))
    if ladoC <=0:
        reise
except:
    print 'Numero precisa ser maior que zero'

if (ladoA != ladoB) and (ladoA != ladoC) and (ladoC != ladoB):
    S = (ladoA+ladoB+ladoC)/float(2)#Semiperimetro
    delta = S*(S-ladoA)*(S-ladoB)*(S-ladoC)
    if delta > 0:
	area = math.sqrt(delta)
    else:
	print ('Valores invalidos')   
elif (ladoA == ladoB) and (ladoA == ladoC) and (ladoC == ladoB):
    area = (math.sqrt(3)/4)*(ladoA**2) 
else:
    if ladoA == ladoB:
        h = math.sqrt(ladoA**2-((ladoC**2)/4))
        area = (h*ladoC)/float(2)
    elif ladoA == ladoC:
        h = math.sqrt(ladoA**2-((ladoB**2)/4))
        area = (h*ladoB)/float(2)
    else:
        h = math.sqrt(ladoB**2-((ladoA**2)/4))
        area = (h*ladoA)/float(2)
print 'A area do triangulo e: '+str(area)
