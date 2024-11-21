def lagrange_interpolacao(x, y, x_val):
    def L(k, x_val):
        termo = 1
        for i in range(len(x)):
            if i != k:
                termo *= (x_val - x[i]) / (x[k] - x[i])
        return termo

    P = 0
    for k in range(len(x)):
        P += y[k] * L(k, x_val)
    return P

# Pontos dados
x = [1, 2, 3]
y = [2, 3, 5]

# Valor a ser interpolado
x_val = 2.5

# Encontrando o valor interpolado
resultado = lagrange_interpolacao(x, y, x_val)
print(f"O valor interpolado em x = {x_val} é: {resultado}")
