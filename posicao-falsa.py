def posicao_falsa(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("O método da posição falsa falhou.")
        return None
    while abs(b - a) > tol:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return b - (f(b) * (b - a)) / (f(b) - f(a))

# Definindo a função
def f(x):
    return x**3 - x - 2

# Intervalo inicial
a = 1
b = 2
tol = 1e-5

# Encontrando a raiz
raiz = posicao_falsa(f, a, b, tol)
print(f"A raiz aproximada é: {raiz}")
