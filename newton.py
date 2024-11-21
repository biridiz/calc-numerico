def newton(f, df, x0, tol, max_iter):
    x_n = x0
    for n in range(max_iter):
        f_xn = f(x_n)
        df_xn = df(x_n)
        if df_xn == 0:
            print("Derivada zero. Não é possível continuar.")
            return None
        x_n1 = x_n - f_xn / df_xn
        if abs(x_n1 - x_n) < tol:
            return x_n1
        x_n = x_n1
    print("Número máximo de iterações atingido.")
    return x_n

# Definindo a função e sua derivada
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

# Parâmetros iniciais
x0 = 1.5
tol = 1e-5
max_iter = 100

# Encontrando a raiz
raiz = newton(f, df, x0, tol, max_iter)
print(f"A raiz aproximada é: {raiz}")
