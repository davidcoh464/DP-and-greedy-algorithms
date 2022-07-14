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
