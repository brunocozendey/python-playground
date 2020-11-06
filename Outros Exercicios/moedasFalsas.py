n = range(1,21)
pos1 = 2
pos2 = 15
k = 1

def Pesa(n,i,f):
  '''
  Função que pesa as moedas de i até f das n moedas
  '''
  peso = len(n[i:f+1])
  if (pos1 in n[i:f+1]):
    peso+=1 
  if (pos2 in n[i:f+1]):
    peso+=1
  return peso

def moedaFalsa(n):
  if (len(n)==1):
    print(n[0])
  else:
    P = Pesa(n,0,((len(n)//2)+1))
    print("Peso:"+str(P))
    print("N:"+str((len(n)//2)+1))
    numMoedas = len(n[0:(len(n)//2)+1])
    print("NumMoedas:"+str(numMoedas)) 
    if (P == ((k*numMoedas)+2)):
      print("Passou 0")
      moedaFalsa(n[0:((len(n)//2))])
    elif (P == ((k*numMoedas)+1)):
      print("passou 1")
      moedaFalsa(n[0:((len(n)//2))])
      print("passou 2")
      moedaFalsa(n[((len(n)//2)):(len(n))])
    else:
      print("Passou 3")
      moedaFalsa(n[((len(n)//2)):(len(n))])

moedaFalsa(n)
        


