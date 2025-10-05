import numpy as np
# implementation of the LU decomposition method for solving systems of linear equations Ax = b

def LUmethod(L,U,b):
    y = np.zeros(shape = 3)
    x = np.zeros(shape = 3)
    #Ly = b
    size = L.shape[0]
    for i in range(0,size):
        Ck = 0
        for k in range(0,i):
            Ck = Ck + y[k]*L[i][k]
        y[i] = (b[i] - Ck)/L[i][i]
        
    #Ux = y
    size = U.shape[0]
    for i in range(0, size):
        Ck = 0
        for k in range(size-i-1, size):
            Ck = Ck + x[k]*U[size-i-1][k]
            
        x[size-i-1] = (y[size-i-1] - Ck)/U[size-i-1][size-i-1]
    
    return x
        
    
def gettingLU(A):
    l = np.zeros(shape = A.shape)
    u = np.zeros(shape = A.shape)
    
    n = l.shape[0]
    for i in range(0,n):
        for j in range(0,n):
            Ck = 0
            for k in range(0,j):
                Ck = Ck + l[i][k]*u[k][j]
            l[i][j] = A[i][j] - Ck
        u[i][i] = 1
        for j in range(i,n):
            Ck = 0
            for k in range(0,i):
                Ck = Ck + l[i][k]*u[k][j]
            u[i][j] = (A[i][j] - Ck)/l[i][i]
    
    return (l,u)
    
A2 = np.array([[4,3,0],[3,4,-1],[0,-1,4]])
b2 = np.array([[7],[8],[6]])

A3 = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
b3 = np.array([[1],[0],[1]])

A4 = np.array([[1,2,1],[2,5,2],[1,2,10]])
b4 = np.array([[4],[12],[13]])

A5 = np.array([[10,2,3],[2,10,5],[3,5,10]])
b5 = np.array([[15],[21],[25]])

print("2")
L, U = gettingLU(A2)
print(LUmethod(L,U,b2))

print("3")
L, U = gettingLU(A3)
print(LUmethod(L,U,b3))

print("4")
L, U = gettingLU(A4)
print(LUmethod(L,U,b4))

print("5")
L, U = gettingLU(A5)
print(LUmethod(L,U,b5))