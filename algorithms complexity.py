import sys
import numpy as np
import operator

# Input:
# matrices dimensions (stored in list `p`)
# numbers of matrices 'n'
def MatrixChainOrder(p, n):
    m = [[0 for x in range(n+1)] for x in range(n+1)]
    s = [[0 for x in range(n+1)] for x in range(n+1)]
    for i in range(1, n+1):
        m[i][i] = 0
    for L in range(2, n+1):
        for i in range(1, n-L + 2):
            j = i + L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    print(" The minimum cost is: "+ str(m[1][n]))
    print(" Optimal matrix multiplication is:")
    printOptimalParens(s,1,n)
    del m[0]
    del s[0]
    for i in range(n):
        del m[i][0]
        del s[i][0]
    print("\n Matrix M is:")
    print(np.matrix(m))
    print(" Matrix S is:")
    print(np.matrix(s)) 

def printOptimalParens(s, i, j):
    if j == i:
        print("A"+str(i), end = "")
    else:
        print("(", end = "")
        printOptimalParens(s,i,s[i][j])
        printOptimalParens(s,s[i][j]+1,j)
        print(")", end = "")



# Input:
# Values (stored in list `v`)
# Weights (stored in list `w`)
# Knapsack capacity `W`
def knapsack_01(v, w, W):
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])
    print(np.matrix(T))


# Input:
# Values (stored in list `v`)
# Weights (stored in list `w`)
# Knapsack capacity `W`
def Greedy_fractional_knapsack(v, w, W):
    d = {}
    for i in range(1,len(v)+1):
        d[i] = v[i-1]/w[i-1]
    d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    weight = 0
    result = []
    for i in d:
        if weight > W:
            break
        elif weight + w[i-1] <= W:
            weight += w[i-1]
            result += [(i,w[i-1])]
        else:
            result += [(i,(W-weight))]
            break
    return result
    
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
    print("Fastest track is : ",end=" ")
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
    s= str(last)+"  "
    i = last
    for j in range(n,1,-1):
        i=pred[i][j]
        s+=str(i)+ "  "
    print(s[::-1])

        
# Function to find the length of the longest common subsequence of substring
def LCSLength(X, Y):
 
    m = len(X)
    n = len(Y)
    
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    print("LCS will be the last entry in the lookup table :",end = "")
    print(T[m][n])
    print("the matrix T is :")
    print(np.matrix(T))

    
        





    

