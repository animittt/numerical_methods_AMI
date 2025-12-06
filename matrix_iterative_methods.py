# implementation of the iterative methods for solving systems of linear equations Ax = b
# Method 1: x = Bx + c (Jacobi method of simple iteration) where B = -D^(-1)(L + U) and c = D^(-1)b where A = D + L + U,
# D - diagonal, L - lower triangular, U - upper triangular
# Method 2: x_i = sum(B_ij * x_j) + c_i (Gauss-Seidel method) uses new values as soon as they are available

import numpy as np

B = np.array([[0, -1/17, -29/34], [-4/11, 0, 1/11], [2/89, 14/89, 0]])
C = np.array([[77/17], [-65/33], [2/89]])
eps = 0.0001

x0 = np.array([[0.], [0.], [0.]])
count_j = 0

while True:
    x1 = np.dot(B, x0) + C
    count_j += 1
    if np.all(np.abs(x1 - x0) < eps):
        break
    x0 = x1

print(f"Корень уравнения (1 метод): {x1}, количество итераций: {count_j}")

# method 2 

x0 = np.array([[0.], [0.], [0.]])
count_g = 0

while True:
    count_g += 1
    x1 = np.copy(x0)
    for i in range(len(x0)):
        x0[i] = np.dot(B[i], x0) + C[i]
    if np.all(np.abs(x1 - x0) < eps):
        break

print(f"Корень уравнения (Метод 2): {x0.T}, количество итераций: {count_g}")