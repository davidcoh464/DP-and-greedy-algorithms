import sys
import numpy as np
import operator

#Running example
#fastestAssemblyTrack([[7,9,3,4,8,4],[8,5,6,4,5,7]],[[2,3,1,3,4,3],[2,1,2,2,1,2]],2,4,3,2,6)
def fastestAssemblyTrack(A,T,e1,e2,x1,x2,n):
    f = [[0 for x in range(n+1)] for x in range(3)] 
    pred = [[0 for x in range(n+1)] for x in range(3)]
    A.insert(0,0)
    T.insert(0,0)
    A[1].insert(0,0)
    A[2].insert(0,0)
    T[1].insert(0,0)
    T[2].insert(0,0)
    f[1][1] = e1+A[1][1]
    f[2][1] = e2+A[2][1]
    pred[1][1] = 1
    pred[2][1] = 2
    def computeValues(j):
        if f[1][j-1] < f[2][j-1]+T[2][j-1]:
                f[1][j] = f[1][j-1]+A[1][j]
                pred[1][j]=1
        else:
             f[1][j] = f[2][j-1]+A[1][j]+T[2][j-1]
             pred[1][j]=2
        if f[2][j-1] < f[1][j-1]+T[1][j-1]:
            f[2][j] = f[2][j-1]+A[2][j]
            pred[2][j]=2
        else:
            f[2][j] = f[1][j-1]+A[2][j]+T[1][j-1]
            pred[2][j]=1
    for j in range(2,n+1):
            computeValues(j)    
    F1 = f[1][n]+x1
    F2 = f[2][n]+x2
    F = F2
    last = 2
    if F1 < F2:
        F=F1
        last = 1
    print("Fastest track is :",end="")
    printFastestTrack(last,n,pred)
    del f[0]
    del pred[0]
    for i in range(2):
        del f[i][0]
        del pred[i][0]
    print("matrix f is:")
    print(np.matrix(f))
    print("matrix pred is:")
    print(np.matrix(pred))
    
def printFastestTrack(last,n,pred):
    s= str(last)+" "
    i = last
    for j in range(n,1,-1):
        i=pred[i][j]
        s+=str(i)+ " "
    print(s[::-1])
