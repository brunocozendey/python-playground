V = [10,3,4,1,2,4,5]

def Quicksort(e,d):
  if (d > e):
    i = e
    j = d
    t = V[((e+d)//2)]  
    
    while (i <= j):
      while (V[i] < t):
        i += 1
      while (V[j] > t):
        j -= 1
      if (i <= j):
        V[i], V[j] = V[j], V[i]
        i+=1
        j-=1
    Quicksort(e,j)
    Quicksort(i,d)

def kPos(V,k):
 '''
 V,k -> n

 Select the k position of vector V
 '''
 Quicksort(0,len(V)-1)
 return(V[k-1])

print(kPos(V,3)) 
