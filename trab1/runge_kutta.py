import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Função definida pelo problema
def f(x, y):
    return (y / x) - (y / x) ** 2

def runge_kutta_method(x0, y0, x_end, h):
    x_values = [x0]
    y_values = [y0]
    while x0 < x_end:
        k1 = f(x0, y0)
        k2 = f(x0 + h / 2, y0 + h / 2 * k1)
        k3 = f(x0 + h / 2, y0 + h / 2 * k2)
        k4 = f(x0 + h, y0 + h * k3)
        y0 += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h
        x_values.append(round(x0, 5))  # Arredondamento para evitar problemas numéricos
        y_values.append(y0)
    return pd.DataFrame({"x": x_values, "y (aproximado)": y_values})

# Condições iniciais
x0, y0 = 1, 1
x_end = 3

# Diferentes valores de h
h_values = [0.25, 0.1, 0.05]

# Soluções usando o método de Runge-Kutta
rk_solutions = {f"h = {h}": runge_kutta_method(x0, y0, x_end, h) for h in h_values}

print(rk_solutions)

# Solução analítica
def analytical_solution(x):
    return x / (1 + np.log(x))

# Valores de x para a solução analítica
x_analytical = np.linspace(1, 3, 500)
y_analytical = analytical_solution(x_analytical)

# Preparar os valores para cada h
colors = {'h = 0.25': 'red', 'h = 0.1': 'blue', 'h = 0.05': 'green'}

# Plot da solução analítica e aproximadas (Runge-Kutta)
plt.figure(figsize=(12, 6))

# Solução analítica
plt.plot(x_analytical, y_analytical, label="Solução analítica", color="black", linestyle="--")

# Soluções aproximadas (Runge-Kutta)
for h_label, solution in rk_solutions.items():
    plt.plot(solution["x"], solution["y (aproximado)"], label=f"Solução {h_label} (RK4)", color=colors[h_label])

plt.title("Solução analítica e soluções aproximadas (Runge-Kutta 4ª ordem)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("images/runge-kutta.png")  # Salvar a figura em um arquivo
plt.close()

# Cálculo do erro para cada h (Runge-Kutta)
plt.figure(figsize=(12, 6))
for h_label, solution in rk_solutions.items():
    # Calcular o erro |y_aproximado - y_analítico|
    y_exact = analytical_solution(np.array(solution["x"]))
    error = np.abs(solution["y (aproximado)"] - y_exact)
    plt.plot(solution["x"], error, label=f"Erro {h_label} (RK4)", color=colors[h_label])

plt.title("Erro das soluções aproximadas em função de x (Runge-Kutta 4ª ordem)")
plt.xlabel("x")
plt.ylabel("Erro absoluto")
plt.legend()
plt.savefig("images/error-runge-kutta.png")  # Salvar a figura em um arquivo
plt.close()