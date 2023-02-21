import random


f = open("INSERT.txt", "a")



for i in range(1,1000000):
    n = []
    for j in range(0,26):
        n.append(random.randrange(0,100,1))
    insert_line = "INSERT INTO t1(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w,y,z) VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11],n[12],n[13],n[14],n[15],n[16],n[17],n[18],n[19],n[20],n[21],n[22],n[23],n[24],n[25])
    f.write(insert_line+";\n")

f.close()
