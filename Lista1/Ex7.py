# -*- coding: cp1252 -*-
joao = jose = maria = pedro = branco = nulo = 0
i=1
while i<=20000:
    voto = int(raw_input('Digite o voto do candidato: '))
    if voto == 1:
        joao +=1
    elif voto == 2:
        jose +=1
    elif voto == 3:
        maria +=1
    elif voto ==4:
        pedro +=1
    elif voto == 0:
        branco +=1
    else: 
        nulo +=1
    i+=1
print 'Quantidade de votos do Joao: '+str(joao) 
print 'Quantidade de votos do Jose: '+str(jose)
print 'Quantidade de votos da Maria: '+str(maria)
print 'Quantidade de votos do Pedro: '+str(pedro)
print 'Quantidade de votos em branco: '+str(branco)
print 'Quantidade de votos nulo: '+str(nulo)
