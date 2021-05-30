#Matriz grafo completo
from main import criar_matriz_zeros, grafo_to_matriz, matriz_to_grafo
from Grafo import Grafo
def matriz_grafo_kn(n):
    M = criar_matriz_zeros(n)
    for lin in range(0,n):
        for col in range(0,n):
            if (lin == col):
                M[lin][col] = 0
            else:
                M[lin][col] = 1
    return M

def matriz_grafo_mycielsky(x,w):
    if (x == w):
        return matriz_grafo_kn(w)
    else:
        mycielsky_menos_1 = matriz_grafo_mycielsky(x-1,w)
        num_vertices = (len(mycielsky_menos_1)*2)+1
        print("vertices",num_vertices)
        print("x", x)
        M = criar_matriz_zeros(num_vertices)
        for i in range(0,num_vertices):
            for j in range(0,num_vertices):
                if ((i < num_vertices-1) and (j < num_vertices-1)):
                    if ((i>len(mycielsky_menos_1)-1) or (j>len(mycielsky_menos_1)-1)):
                        M[i][j] = mycielsky_menos_1[i-len(mycielsky_menos_1)][j-len(mycielsky_menos_1)]
                    else:
                        M[i][j] = mycielsky_menos_1[i][j]     
                else:
                    if ((i<len(mycielsky_menos_1)) or (j<len(mycielsky_menos_1)) or (j==i)):
                        M[i][j] = 0
                    else:
                        M[i][j] = 1
        return M


def get_grau_max(g):
    M = grafo_to_matriz(g)
    calc_max = lambda a, b: max([a,b])
    grau_max = 0
    for i in range(0,len(M)):
        calcula_grau = 0
        for j in range(0,len(M)):
            calcula_grau += M[i][j]
        grau_max = calc_max(grau_max,calcula_grau)
    return grau_max


def get_neighbor(arestas,v):
    n = []
    for (v1,v2) in arestas:
        if (v1 == v):
            n.append(v2)
    return n
        

def get_coloracao(g):
    vertices = g.get_vertices()
    vertices.sort()
    print("vertices",vertices)
    cores = list(range(2,(get_grau_max(g)+2)))
    c = [0]*len(vertices)
    c[0] = 1
    print("c",c)
    print(g.get_arestas())
    for i in range(1,len(vertices)):
        aux_cores = cores.copy()
        neighbors = get_neighbor(g.get_arestas(),i+1)
        print("cd", aux_cores)
        print("viz",neighbors)
        for n in neighbors:
            if ( c[n-1] in aux_cores):
                aux_cores.remove(c[n-1])
        print("ac", aux_cores)
        c[i] = min(aux_cores)
    return c
        





    

arestas = [(1,2),(1,4),(1,3),(2,1),(2,3),(3,2),(3,1),(3,4),(4,1),(4,3)]
grafo = Grafo(arestas)
print(get_coloracao(grafo))