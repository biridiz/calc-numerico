def secante(f, x0, x1, tol, max_iter):
    for n in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Divisão por zero. Método falhou.")
            return None
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    print("Número máximo de iterações atingido.")
    return x1

# Definindo a função
def f(x):
    return x**3 - x - 2

# Parâmetros iniciais
x0 = 1
x1 = 2
tol = 1e-5
max_iter = 100

# Encontrando a raiz
raiz = secante(f, x0, x1, tol, max_iter)
print(f"A raiz aproximada é: {raiz}")
