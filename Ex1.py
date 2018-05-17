# -*- coding: cp1252 -*-
idade = maior_salario = total_salario_F = total_salario_M = 0
total_F = total_M = 1
while True:
    idade = int(raw_input("Qual a idade?"))
    if idade <0:
        break
    while True:
        sexo = raw_input("Qual sexo[M/F]?")
        if (sexo == 'M') or (sexo=='F'):
            break
    salario = int(raw_input("Qual o salario?"))
    if idade < 30:
        if salario > maior_salario:
            maior_salario = salario
    if sexo == 'M':
        total_M +=1
        total_salario_M += salario
    if sexo == 'F':
        total_F +=1
        total_salario_F += salario    
print 'O maior salario para >30 e: '+str(maior_salario)
print 'A media de salario Masculina e: '+str(total_salario_M/float(total_M))
print 'A media de salario Feminina e: '+str(total_salario_F/float(total_F))