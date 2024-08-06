import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

# Функция для обработки данных
def process_data(x, y, index):
    # Проверяем, что длины массивов совпадают
    assert len(x) == len(y), f"Массивы x{index} и y{index} должны быть одинаковой длины"
    
    # Сортируем данные по возрастанию x
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    
    # Фильтруем положительные значения x и соответствующие им y
    positive_mask = x_sorted > 0
    x_positive = x_sorted[positive_mask]
    y_positive = y_sorted[positive_mask]
    
    # Проверяем, что после фильтрации есть данные
    assert len(x_positive) > 0, f"Нет положительных значений в x{index}"
    
    # Преобразование x с помощью натурального логарифма
    log_x_positive = np.log(x_positive)
    
    # Проверяем на NaN и бесконечности в x и y
    assert not np.any(np.isnan(log_x_positive)), f"Есть значения NaN в log_x{index}_positive"
    assert not np.any(np.isinf(log_x_positive)), f"Есть бесконечные значения в log_x{index}_positive"
    assert not np.any(np.isnan(y_positive)), f"Есть значения NaN в y{index}_positive"
    assert not np.any(np.isinf(y_positive)), f"Есть бесконечные значения в y{index}_positive"
    
    # Удаляем некорректные значения из y_positive и соответствующие им x
    finite_mask_y = np.isfinite(y_positive)
    x_positive = x_positive[finite_mask_y]
    y_positive = y_positive[finite_mask_y]
    log_x_positive = log_x_positive[finite_mask_y]
    
    # Проверяем, что после удаления некорректных значений остались данные
    assert len(y_positive) > 0, f"После удаления некорректных значений нет данных в y{index}_positive"
    
    # Аппроксимация монотонным кубическим сплайном
    spline = PchipInterpolator(log_x_positive, y_positive)
    
    # Точки для графика
    log_x_fit = np.linspace(min(log_x_positive), max(log_x_positive), 1000)
    y_fit = spline(log_x_fit)
    x_fit = np.exp(log_x_fit)  # Преобразуем обратно в масштаб x
    
    return x_positive, y_positive, x_fit, y_fit

# Загрузка данных из файла Excel
data = pd.read_excel('data_.xlsx')
x1 = data['Ток'].values
y1 = data['Значение'].values
x2 = data['Ток2'].values
y2 = data['Значение2'].values
x3 = data['Ток3'].values
y3 = data['Значение3'].values

# Обработка данных для каждого набора
x1_positive, y1_positive, x1_fit, y1_fit = process_data(x1, y1, index=1)
x2_positive, y2_positive, x2_fit, y2_fit = process_data(x2, y2, index=2)
x3_positive, y3_positive, x3_fit, y3_fit = process_data(x3, y3, index=3)

# Напряжение U = 300 В
U1 = 0.3  # Вольт
U2 = 0.1
# Функция для вычисления токов, сопротивлений и dT
def compute_R_and_dT1(y_positive, U):
    # y_positive в мА, конвертируем в А
    y_positive_in_A = y_positive / 1000.0  # Переводим мА в А
    I_max = np.max(y_positive_in_A)
    I_min = np.min(y_positive_in_A)
    R_max = U / I_min if I_min != 0 else np.inf
    R_min = U / I_max if I_max != 0 else np.inf
    # Вычисляем dT
    dT = (R_max - R_min) / (684.744 * 0.004)
    return I_min * 1000.0, I_max * 1000.0, R_min, R_max, dT  # Токи возвращаем в мА
def compute_R_and_dT2(y_positive, U):
    # y_positive в мА, конвертируем в А
    y_positive_in_A = y_positive / 1000.0  # Переводим мА в А
    I_max = np.max(y_positive_in_A)
    I_min = np.min(y_positive_in_A)
    R_max = 1000*U / I_min if I_min != 0 else np.inf
    R_min = 1000*U / I_max if I_max != 0 else np.inf
    # Вычисляем dT
    dT = (R_max - R_min) / (1900 * 0.004)
    return I_min * 1000.0, I_max * 1000.0, R_min, R_max, dT  # Токи возвращаем в мА
# Вычисления для каждого набора данных
I1_min, I1_max, R1_min, R1_max, dT1 = compute_R_and_dT1(y1_positive, U1)
I2_min, I2_max, R2_min, R2_max, dT2 = compute_R_and_dT2(y2_positive, U2)
I3_min, I3_max, R3_min, R3_max, dT3 = compute_R_and_dT1(y3_positive, U1)

# Создаем фигуру с несколькими подграфиками
fig, axs = plt.subplots(3, 2, figsize=(12, 6))

# ===== Графики для набора данных 1 =====
# Линейный масштаб
axs[0, 0].plot(x1_positive, y1_positive, 'o')
axs[0, 0].plot(x1_fit, y1_fit, '-')
axs[0, 0].set_xlabel('Давление (мбар)')
axs[0, 0].set_ylabel('Ток (мА)')
axs[0, 0].set_title('График 23.09.2024 (образец №2) (линейный масштаб)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Добавляем текст с диапазоном тока, сопротивления и dT
textstr1 = '\n'.join((
    f'I_min = {I1_min:.3f} мА',
    f'I_max = {I1_max:.3f} мА',
    f'R_min = {R1_min:.3f} Ом',
    f'R_max = {R1_max:.3f} Ом',
    f'dT = {dT1:.4f}',
))
axs[0, 0].text(0.65, 0.85, textstr1, transform=axs[0, 0].transAxes, fontsize=10,
               verticalalignment='top', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Логарифмический масштаб по x
axs[0, 1].plot(x1_positive, y1_positive, 'o')
axs[0, 1].plot(x1_fit, y1_fit, '-' )
axs[0, 1].set_xlabel('Давление (мбар)')
axs[0, 1].set_ylabel('Ток (мА)')
axs[0, 1].set_title('График 23.09.2024 (образец №2) (логарифмический масштаб по x)')
axs[0, 1].set_xscale('log')
axs[0, 1].legend()
axs[0, 1].grid(True)
axs[0, 1].text(0.35, 0.35, textstr1, transform=axs[0, 1].transAxes, fontsize=8,
               verticalalignment='bottom', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ===== Графики для набора данных 2 =====
# Линейный масштаб
axs[1, 0].plot(x2_positive, y2_positive, 'o')
axs[1, 0].plot(x2_fit, y2_fit, '-')
axs[1, 0].set_xlabel('Давление (мбар)')
axs[1, 0].set_ylabel('Ток (мА)')
axs[1, 0].set_title('График 21.08.2024 (образец №3) (линейный масштаб)')
axs[1, 0].legend()
axs[1, 0].grid(True)

textstr2 = '\n'.join((
    f'I_min = {I2_min:.3f} мкА',
    f'I_max = {I2_max:.3f} мкА',
    f'R_min = {R2_min:.3f} Ом',
    f'R_max = {R2_max:.3f} Ом',
    f'dT = {dT2:.4f}',
))
axs[1, 0].text(0.65, 0.78, textstr2, transform=axs[1, 0].transAxes, fontsize=10,
               verticalalignment='top', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Логарифмический масштаб по x
axs[1, 1].plot(x2_positive, y2_positive, 'o')
axs[1, 1].plot(x2_fit, y2_fit, '-')
axs[1, 1].set_xlabel('Давление (мбар)')
axs[1, 1].set_ylabel('Ток (мА)')
axs[1, 1].set_title('График 21.08.2024 (образец №3) (логарифмический масштаб по x)')
axs[1, 1].set_xscale('log')
axs[1, 1].legend()
axs[1, 1].grid(True)
axs[1, 1].text(0.25, 0.45, textstr2, transform=axs[1, 1].transAxes, fontsize=6,
               verticalalignment='bottom', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ===== Графики для набора данных 3 =====
# Линейный масштаб
axs[2, 0].plot(x3_positive, y3_positive, 'o')
axs[2, 0].plot(x3_fit, y3_fit, '-')
axs[2, 0].set_xlabel('Давление (мбар)')
axs[2, 0].set_ylabel('Ток (мА)')
axs[2, 0].set_title('График 25.09.2024 (образец №1) (линейный масштаб)')
axs[2, 0].legend()
axs[2, 0].grid(True)

textstr3 = '\n'.join((
    f'I_min = {I3_min:.3f} мА',
    f'I_max = {I3_max:.3f} мА',
    f'R_min = {R3_min:.3f} Ом',
    f'R_max = {R3_max:.3f} Ом',
    f'dT = {dT3:.4f}',
))
axs[2, 0].text(0.65, 0.15, textstr3, transform=axs[2, 0].transAxes, fontsize=8,
               verticalalignment='bottom', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Логарифмический масштаб по x
axs[2, 1].plot(x3_positive, y3_positive, 'o')
axs[2, 1].plot(x3_fit, y3_fit, '-')
axs[2, 1].set_xlabel('Давление (мбар)')
axs[2, 1].set_ylabel('Ток (мА)')
axs[2, 1].set_title('График 25.09.2024 (образец №1) (логарифмический масштаб по x)')
axs[2, 1].set_xscale('log')
axs[2, 1].legend()
axs[2, 1].grid(True)
axs[2, 1].text(0.25, 0.45, textstr3, transform=axs[2, 1].transAxes, fontsize=6,
               verticalalignment='baseline', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
