def bisseccao(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("O método da bissecção falhou.")
        return None
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# Definindo a função
def f(x):
    return x**3 - x - 2

# Intervalo inicial
a = 1
b = 2
tol = 1e-5

# Encontrando a raiz
raiz = bisseccao(f, a, b, tol)
print(f"A raiz aproximada é: {raiz}")
