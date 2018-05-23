# -*- coding: cp1252 -*-
'''
Esse programa criptografa e decriptografa uma mensagem seguindo o seguinte padrão:
Soma 1 ao código ascci de cada letra ou caracter.
E no final exibi o texto lido, criptografado e decriptografado.

Criado por: Bruno Cozendey
Em: 23/05/2018
'''
def ler():
    while True:
        try:    
            frase = raw_input('Digite a frase que será criptografada: \n')
            break
        except:
            print 'Oops saiu algo errado!'
    return frase

def cript(frase):
    frase_cript = ''
    for i in frase:
        frase_cript += chr(ord(i)+1)
    return frase_cript

def decript(frase):
    frase_decript = ''
    for i in frase:
        frase_decript += chr(ord(i)-1)
    return frase_decript

def impr(frase,frase_cript,frase_decript):
    print 'A sua string é \'{:1s}\'. \n Criptografada: {:1s}. \n Decriptografada:{:1s}.'.format(frase,frase_cript,frase_decript)

#Main
frase = ler()
frase_cript = cript(frase)
frase_decript = decript(frase_cript)
impr(frase, frase_cript,frase_decript)
