import numpy as np
import matplotlib.pyplot as plt

def solve_pvc(h):
    # Definir o intervalo e os pontos da malha
    x = np.arange(0, 1 + h, h)
    n = len(x)
    
    # Matriz e vetor do sistema linear
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Condições de contorno
    A[0, 0] = 1  # y(0) = 0
    A[-1, -1] = 1  # y(1) = e
    b[-1] = np.e  # Valor de y(1)
    
    # Preenchendo a matriz para os pontos internos
    for i in range(1, n - 1):
        A[i, i - 1] = 1 / h**2 - 1 / (2 * h)
        A[i, i] = -2 / h**2 + x[i]
        A[i, i + 1] = 1 / h**2 + 1 / (2 * h)
        b[i] = -np.exp(x[i]) * (x[i]**2 + 1)
    
    # Resolver o sistema linear
    y = np.linalg.solve(A, b)
    return x, y

# Valores de h
h_values = [0.1, 0.05, 0.01]
solutions = []

# Resolver o PVC para cada h
for h in h_values:
    solutions.append(solve_pvc(h))

# Plotar os resultados
plt.figure(figsize=(10, 6))
for (x, y), h in zip(solutions, h_values):
    plt.plot(x, y, label=f"h = {h:.2f}")

plt.title("Solução do PVC usando diferenças finitas")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.savefig("images/diff.png")  # Salvar a figura em um arquivo
plt.close()
