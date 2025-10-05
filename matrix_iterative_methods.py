# implementation of the iterative methods for solving systems of linear equations Ax = b
# Method 1: x = Bx + c (Jacobi method)
# Method 2: x_i = sum(B_ij * x_j) + c_i (Gauss-Seidel method)

import numpy as np

b = np.array([[0, (-5/76), (-24/76)], [(-4/66), 0, 2/66], [(-18/46), (-25/46), 0]])
c = np.array([[19/76], [75/76], [22/46]])


x0 = np.array([[0.], [0.], [0.]])
count_j = 0

while True:
    x1 = np.dot(b, x0) + c
    count_j += 1
    if np.all(np.abs(x1 - x0) < 0.001):
        break
    x0 = x1

print(f"Корень уравнения (1 метод): {x1}, количество итераций: {count_j}")

x0 = np.array([[0.], [0.], [0.]])
count_g = 0

while True:
    count_g += 1
    x1 = np.copy(x0)
    for i in range(len(x0)):
        x0[i] = np.dot(b[i], x0) + c[i]
    if np.all(np.abs(x1 - x0) < 0.001):
        break

print(f"Корень уравнения (Метод 2): {x0.T}, количество итераций: {count_g}")