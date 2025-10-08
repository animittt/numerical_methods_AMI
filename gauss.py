# implementation of the gauss method for solving linear systems Ax = b

import numpy as np
from numpy.linalg import LinAlgError


def gauss(A, b):
    """
    Solve the linear system Ax = b using Gaussian elimination with partial pivoting.

    Parameters:
    A : array_like, shape (n, n)
        Coefficient matrix.
    b : array_like, shape (n,)
        Ordinate or "dependent variable" values.

    Returns:
    x : ndarray, shape (n,)
        Solution to the system Ax = b.

    Raises:
    LinAlgError
        If the matrix A is singular or not square.
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = A.shape[0]
    if A.shape[1] != n or b.size != n:
        raise LinAlgError("Matrix A must be square and vector b must have compatible dimensions.")

    # Forward elimination with partial pivoting
    for k in range(n):
        # Find the pivot row
        max_row_index = np.argmax(np.abs(A[k:n, k])) + k
        if A[max_row_index, k] == 0:
            raise LinAlgError("Matrix is singular.")
        
        # Swap the current row with the pivot row
        if max_row_index != k:
            A[[k, max_row_index]] = A[[max_row_index, k]]
            b[[k, max_row_index]] = b[[max_row_index, k]]

        # Eliminate entries below the pivot
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:
            raise LinAlgError("Matrix is singular.")
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# Example usage:
A = [[2, 1, -1, 3],
     [1, 3, 2, -1],
     [3, 1, 4, 2],
     [1, -1, 1, 2]]

b = [9, 1, 13, 3]
solution = gauss(A, b)
print("Solution:", solution)
