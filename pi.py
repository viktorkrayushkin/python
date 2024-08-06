import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# Загрузка данных из Excel файлов
excel_files = [
    ('output_0.00032mbar_10000.xlsx', '10 секунд 3.2*10^-4 mBar'),
    ('output_0.0018mbar.xlsx', '10 секунд 1.8*10^-3 mBar'),
    #('output_air.xlsx', '10 секунд 1000 mBar'),
    ('output_0.00014mbar_10000.xlsx', '10 секунд 1.4*10^-4 mBar'),
    ('output_0.013mbar_10000.xlsx', '10 секунд 1.3*10^-2 mBar'),
    ('output_0.0013mbar_10000.xlsx', '10 секунд 1.3*10^-3 mBar'),
    ('output_0.237mbar_10000.xlsx', '10 секунд 2.37*10^-1 mBar'),
    ('output_1.2mbar_10000.xlsx', '10 секунд 1.2 mBar'),
    ('output_0.0113mbar_10000.xlsx', '10 секунд 1.13*10^-2 mBar')
]

data = {}

# Предполагается, что во всех файлах есть столбец 't'
df = pd.read_excel(excel_files[0][0], sheet_name='Sheet1')
data['x'] = df['t']

# Чтение каждого файла и сохранение данных 'I'
for file_name, label in excel_files:
    df = pd.read_excel(file_name, sheet_name='Sheet1')
    data[label] = -df['I'] * 1000  # Умножаем на 1000 и берем отрицательное значение

df = pd.DataFrame(data)

# Фильтруем данные, исключая время <= 0.005 секунд
df_filtered = df[df['x'] > 0.005].copy()

# Определяем стиль для каждого набора данных
plot_styles = [
    ('blue', 'o', '-', 0),
    ('green', 's', '--', 0),
    ('red', '^', '-.', 0),
    ('orange', 'D', '-', 0),
    ('lime', 'v', '--', 0),
    ('purple', '*', '-.', 0),
    ('forestgreen', 'x', '-', 0),
    ('gold', 'h', '--', 0),
    ('lightgrey', '+', '-.', 0)
]

# Инициализируем словарь для хранения результатов аппроксимации
fit_results = {}

# Определяем функцию экспоненциального затухания
def exponential_decay(t, I0, lambd):
    return I0 * np.exp(-lambd * t)

# Выполняем экспоненциальное приближение для каждого набора данных
for label in list(data.keys())[1:]:
    y = df_filtered[label]
    x = df_filtered['x']
    # Убедимся, что I > 0 перед аппроксимацией
    mask = y > 0
    y_positive = y[mask]
    x_positive = x[mask]
    # Выполняем экспоненциальное приближение
    try:
        popt, pcov = curve_fit(exponential_decay, x_positive, y_positive, p0=(max(y_positive), 1))
        I0, lambd = popt
        fit_results[label] = {'I0': I0, 'lambda': lambd}
        # Вычисляем приближенные значения I
        df_filtered.loc[mask, 'fit_' + label] = exponential_decay(x_positive, *popt)
    except RuntimeError:
        print(f"Не удалось выполнить аппроксимацию для {label}")

# Строим график I(t) с логарифмическим масштабом по оси Y и приближенными кривыми
plt.figure(figsize=(12, 8))

for (label, (color, marker, linestyle, markersize)) in zip(list(data.keys())[1:], plot_styles):
    x_plot = df_filtered['x'][df_filtered[label].notnull()]
    y_plot = df_filtered[label][df_filtered[label].notnull()]
    y_fit_label = 'fit_' + label
    y_fit = df_filtered[y_fit_label][df_filtered[y_fit_label].notnull()] if y_fit_label in df_filtered else None
    plt.plot(x_plot, y_plot, marker=marker, linestyle='', color=color, markersize=markersize, label=label)
    if y_fit is not None:
        plt.semilogy(x_plot, y_fit, linestyle=linestyle, color=color, label=label + ' Аппроксимация')

# Устанавливаем логарифмический масштаб по оси Y
plt.yscale('log')

# Настраиваем график
plt.xlabel('t, с')
plt.ylabel('I, мА')
plt.title('I(t) и экспоненциальные аппроксимации, Амплитуда импульса 7 В')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Выводим результаты аппроксимации
for label, fit in fit_results.items():
    print(f"Результаты аппроксимации для {label}:")
    print(f"  I0 (начальный ток): {fit['I0']}")
    print(f"  Lambda (постоянная затухания): {fit['lambda']}")
    print()
