import numpy as np
import pandas as pd

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n deve ser par para a Regra de Simpson")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    
    integral *= h / 3
    return integral

def f(x):
    return np.exp(-x**2)

def g(x):
    return np.log(x + np.sqrt(x + 1))

def adaptive_simpsons_rule(f, a, b, epsilon=1e-3):
    n = 2
    current_integral = simpsons_rule(f, a, b, n)
    error = float('inf')
    points_table = []

    while error > epsilon:
        n *= 2  # Dobrar o número de subintervalos para maior precisão
        previous_integral = current_integral
        current_integral = simpsons_rule(f, a, b, n)
        
        # Calcular erro como diferença entre aproximações consecutivas
        error = abs(current_integral - previous_integral)
        
        h = (b - a) / n
        points_table = [(a + i * h, f(a + i * h)) for i in range(n + 1)]

    return current_integral, points_table

def adaptive_trapezoidal_rule(f, a, b, epsilon=1e-3):
    n = 1  # Começamos com n=1 subintervalo
    current_integral = trapezoidal_rule(f, a, b, n)
    error = float('inf')
    points_table = []

    while error > epsilon:
        n *= 2  # Dobrar o número de subintervalos para maior precisão
        previous_integral = current_integral
        current_integral = trapezoidal_rule(f, a, b, n)
        
        # Calcular erro como diferença entre aproximações consecutivas
        error = abs(current_integral - previous_integral)
        
        h = (b - a) / n
        points_table = [(a + i * h, f(a + i * h)) for i in range(n + 1)]

    return current_integral, points_table

# Intervalo de integração e precisão desejada
a = 0
b = 1
epsilon = 1e-3

# Calculando a integral e os pontos usando a Regra do Trapézio
trapezoidal_result, trapezoidal_points_table = adaptive_trapezoidal_rule(g, a, b, epsilon)
# Convertendo os pontos em DataFrame para exibir como tabela
trapezoidal_points_df = pd.DataFrame(trapezoidal_points_table, columns=["xi", "yi"])
print(trapezoidal_result, trapezoidal_points_df)

# Calculando a integral e os pontos
integral_result, points_table = adaptive_simpsons_rule(g, a, b, epsilon)
# Convertendo os pontos em DataFrame para exibir como tabela
points_df = pd.DataFrame(points_table, columns=["xi", "yi"])
print(integral_result, points_df)