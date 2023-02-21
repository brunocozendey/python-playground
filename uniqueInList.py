# -*- encoding: utf-8 -*-

# Definir o elemento único no array, tem pelo menos 3

def find_uniq(arr):
    arr.sort()
    for i in range(1,len(arr)-1):
        if arr[0] != arr[1]: return arr[0]
        if ((arr[i] != arr[i-1]) and (arr[i] != arr[i+1])): return arr[i]
        if ((arr[len(arr)-1]) != (arr[len(arr)-2])): return arr[len(arr)-1]   
        #print arr[i]


#main

print( find_uniq([ 1, 1, 1, 2, 1, 1 ]))


#Best Pratice
def find_uniq_bpx(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b