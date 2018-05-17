# -*- coding: cp1252 -*-
sim = nao = 0
while True:
    try:
        resposta = raw_input('Voce esta satisfeito?[S/N]')
        if resposta == 'S' or resposta == 's':
            sim +=1
        elif resposta == 'N' or resposta == 'n':
            nao +=1
        elif resposta == 'F' or resposta == 'f':
            break
        else:
            reise

    except:
        print "Responda S ou N!"
print 'Quantidade de respostas Sim: '+str(sim)
print 'Quantidade de respostas Nao: '+str(nao)