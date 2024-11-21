import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
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

sol_gauss_seidel = gauss_seidel(A, b, x0, tol, max_iter)
print(f"Solução pelo método de Gauss-Seidel: {sol_gauss_seidel}")