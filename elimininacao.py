import numpy as np

def eliminacao_gauss(A, b):
    n = len(b)
    # Matriz estendida
    M = np.hstack((A, b.reshape(-1, 1)))
    
    # Eliminação
    for i in range(n):
        # Pivoteamento
        for k in range(i+1, n):
            if M[i, i] == 0:
                M[[i, k]] = M[[k, i]]
            factor = M[k, i] / M[i, i]
            M[k, i:] -= factor * M[i, i:]
    
    # Substituição Regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    
    return x

def eliminacao_gauss_jordan(A, b):
    n = len(b)
    # Matriz estendida
    M = np.hstack((A, b.reshape(-1, 1)))
    
    # Eliminação
    for i in range(n):
        # Pivoteamento
        if M[i, i] == 0:
            for k in range(i+1, n):
                if M[k, i] != 0:
                    M[[i, k]] = M[[k, i]]
                    break
        M[i] = M[i] / M[i, i]
        for k in range(n):
            if k != i:
                M[k] -= M[k, i] * M[i]
    
    # Soluções
    x = M[:, -1]
    return x

# Exemplo de uso
A = np.array([[2, 3, 1], [4, 1, -2], [3, 2, 3]], dtype=float)
b = np.array([1, -2, 3], dtype=float)

sol_gauss = eliminacao_gauss(A, b)
sol_gauss_jordan = eliminacao_gauss_jordan(A, b)

print(f"Solução pelo método de Gauss: {sol_gauss}")
print(f"Solução pelo método de Gauss-Jordan: {sol_gauss_jordan}")
