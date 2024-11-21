# Diferenças Divididas
def diferencas_divididas(x, y):
    n = len(y)
    coef = [0] * n
    coef[0] = y[0]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
        coef[j] = y[j]
    return coef

# Pontos dados
x = [1, 2, 3]
y = [2, 3, 5]

# Calculando coeficientes das diferenças divididas
coef = diferencas_divididas(x, y)
print(f"Coeficientes das diferenças divididas: {coef}")

# Diferenças Finitas
def diferenca_finita_progressiva(f, x, h):
    return (f(x + h) - f(x)) / h

def diferenca_finita_regressiva(f, x, h):
    return (f(x) - f(x - h)) / h

def diferenca_finita_centrada(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Função a ser derivada
def f(x):
    return x**2

# Ponto e passo
x_val = 1
h = 0.1

# Calculando diferenças finitas
progressiva = diferenca_finita_progressiva(f, x_val, h)
regressiva = diferenca_finita_regressiva(f, x_val, h)
centrada = diferenca_finita_centrada(f, x_val, h)

print(f"Diferença finita progressiva: {progressiva}")
print(f"Diferença finita regressiva: {regressiva}")
print(f"Diferença finita centrada: {centrada}")
