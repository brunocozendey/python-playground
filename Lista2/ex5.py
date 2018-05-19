# -*- coding: cp1252 -*-
'''
Esse programa lê e valida as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
def ler():
    while True:
        try:    
            nome = raw_input('Digite seu nome: \n')
            if len(nome)<3:
                reise
            else:
                break
        except:
            print 'O nome precisa ter mais que 3 caracteres!'
    while True:
        try:    
            idade = int(raw_input('Digite sua idade: \n'))
            if idade < 1 and idade > 150:
                reise
            else:
                break
        except:
            print 'Sua idade deve estar entre 0 e 150 anos!'
    while True:
        try:    
            salario = int(raw_input('Digite seu salário: \n'))
            if salario < 1:
                reise
            else:
                break
        except:
            print 'Seu salário precisa ser maior que 0'
    while True:
        try:    
            sexo = raw_input('Digite seu sexo [m/f]: \n')
            if sexo not in ['m','M','F','f']:
                reise
            else:
                break
        except:
            print 'Digite m para masculino ou f para feminino.'
    while True:
        try:    
            estado = raw_input('Digite seu estado civil: s-solteiro, c-casado, v-viúvo ou d-divorciado \n')
            if estado not in ['s','S','c','C','V','v','D','d']:
                reise
            else:
                break
        except:
            print 'Digite s ou c ou v ou d.'
    return nome,idade,salario,sexo,estado

def impr(nome,idade,salario,sexo,estado):
    print 'Seu nome é {:1s}, possui {:d} anos, seu salário é de R${:06.2f}, você é do sexo {:1s} e seu estado civil é {:1s}'.format(nome,idade,salario,sexo,estado)

#Main
nome,idade,salario,sexo,estado = ler()
impr(nome,idade,salario,sexo,estado)
