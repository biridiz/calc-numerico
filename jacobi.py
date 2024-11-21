import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x

# Exemplo de uso
A = np.array([[4, 1, 1], [1, 5, 2], [2, 2, 6]], dtype=float)
b = np.array([4, -4, 6], dtype=float)
x0 = np.zeros_like(b)
tol = 1e-5
max_iter = 100

sol_jacobi = jacobi(A, b, x0, tol, max_iter)

print(f"Solução pelo método de Jacobi: {sol_jacobi}")
