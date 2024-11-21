def newton_interpolacao(x, y, x_val):
    def diferencas_divididas(x, y):
        n = len(y)
        coef = [0] * n
        coef[0] = y[0]
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
            coef[j] = y[j]
        return coef

    coef = diferencas_divididas(x, y)
    n = len(coef)
    P = coef[n - 1]
    for k in range(n - 2, -1, -1):
        P = P * (x_val - x[k]) + coef[k]
    return P

# Pontos dados
x = [1, 2, 3]
y = [2, 3, 5]

# Valor a ser interpolado
x_val = 2.5

# Encontrando o valor interpolado
resultado = newton_interpolacao(x, y, x_val)
print(f"O valor interpolado em x = {x_val} é: {resultado}")
