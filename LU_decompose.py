import numpy as np
# implementation of the LU decomposition method for solving systems of linear equations Ax = b

def LU_solve(L, U, b):
    n = L.shape[0]

    # Forward substitution: L y = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]   # <-- divide by L[i,i]

    # Backward substitution: U x = y
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x
        
    
def LU_decomposition(A):
  n = A.shape[0]
  L = np.zeros((n, n))
  U = np.zeros((n, n))

  for i in range(n):

    for j in range(i + 1):
      sum_lu = sum(L[i, k] * U[k, j] for k in range(j))
      L[i, j] = A[i, j] - sum_lu

    U[i, i] = 1
    for j in range(i + 1, n):
      sum_lu = sum(L[i, k] * U[k, j] for k in range(i))
      U[i, j] = (A[i, j] - sum_lu) / L[i, i]
  return L, U

A = np.array([
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]])
b = np.array([[2], [-1], [4]])

A2 = np.array([[4,3,0],[3,4,-1],[0,-1,4]])
b2 = np.array([[7],[8],[6]])

A3 = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
b3 = np.array([[1],[0],[1]])

A4 = np.array([[1,2,1],[2,5,2],[1,2,10]])
b4 = np.array([[4],[12],[13]])

A5 = np.array([[10,2,3],[2,10,5],[3,5,10]])
b5 = np.array([[15],[21],[25]])

print("1")
L, U = LU_decomposition(A)
print(LU_solve(L,U,b))

print("2")
L, U = LU_decomposition(A2)
print(LU_solve(L,U,b2))

print("3")
L, U = LU_decomposition(A3)
print(LU_solve(L,U,b3))

print("4")
L, U = LU_decomposition(A4)
print(LU_solve(L,U,b4))

print("5")
L, U = LU_decomposition(A5)
print(LU_solve(L,U,b5))