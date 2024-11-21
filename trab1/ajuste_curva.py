import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data_folder = '/home/luiz/calc-numerico/trab1/data'
files = os.listdir(data_folder)
df = {}

for csv_file in files:
  file_path = os.path.join(data_folder, csv_file)
  df[csv_file] = pd.read_csv(file_path)
  df[csv_file] = df[csv_file][['Height(cm.)', 'Weight(lbs.)']]

combined_df = pd.concat(df.values(), ignore_index=True)

X = combined_df['Height(cm.)']
Y = combined_df['Weight(lbs.)']
slope, intercept = np.polyfit(X, Y, 1)
print(f"y = {slope}x + {intercept}")

def exp_func(x, a, b):
    return a * np.exp(b * x)

params, _ = curve_fit(exp_func, X, Y)
a_exp, b_exp = params

def power_func(x, a, b):
    return a * x ** b

params, _ = curve_fit(power_func, X, Y)
a_pow, b_pow = params 

degree = 4
coeffs = np.polyfit(X, Y, degree)
poly_eq = np.poly1d(coeffs)

y_mean = Y.mean()
y_pred_linear = slope * X + intercept
ss_res_linear = np.sum((Y - y_pred_linear) ** 2)  # Soma dos quadrados dos resíduos
ss_tot = np.sum((Y - y_mean) ** 2)  # Soma total dos quadrados
r2_linear = 1 - (ss_res_linear / ss_tot)
y_pred_exp = exp_func(X, a_exp, b_exp)
ss_res_exp = np.sum((Y - y_pred_exp) ** 2)
r2_exp = 1 - (ss_res_exp / ss_tot)
y_pred_pow = power_func(X, a_pow, b_pow)
ss_res_pow = np.sum((Y - y_pred_pow) ** 2)
r2_pow = 1 - (ss_res_pow / ss_tot)
y_pred_poly = poly_eq(X)
ss_res_poly = np.sum((Y - y_pred_poly) ** 2)
r2_poly = 1 - (ss_res_poly / ss_tot)

print(f"R² do Ajuste Linear: {r2_linear:.4f}")
print(f"R² do Ajuste Exponencial: {r2_exp:.4f}")
print(f"R² do Ajuste de Potência: {r2_pow:.4f}")
print(f"R² do Ajuste Polinomial (Grau {degree}): {r2_poly:.4f}")

plt.scatter(X, Y, color='blue', label='Dados Originais')

x_values = np.linspace(X.min(), X.max(), 100)
y_linear = slope * x_values + intercept
plt.plot(x_values, y_linear, color='red', label='Curva Linear')

y_pow = power_func(x_values, a_pow, b_pow)
plt.plot(x_values, y_pow, color='purple', label='Curva de Potência')

y_poly = poly_eq(x_values)
plt.plot(x_values, y_poly, color='orange', label=f'Curva Polinomial (Grau {degree})')

plt.xlabel('Altura (cm)')
plt.ylabel('Peso (lbs)')
plt.title('Ajustes Lineares, Exponenciais, de Potência e Polinomiais para Altura e Peso de todos os jogadores do FIFA23')
plt.legend()
plt.show()
