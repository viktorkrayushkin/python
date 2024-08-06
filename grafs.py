import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Загрузка данных из файла 'data_1.txt'
data1 = np.loadtxt('data_1.txt', delimiter='t')
x1 = data1[:, 0]
y1 = data1[:, 1]

# Read the data, specifying 'NA' as a missing value indicator
data = pd.read_csv('data.txt', sep='\s+', header=None)
data_1 = pd.read_csv('2_den_3.txt', sep='\s+', header=None)
data_2 = pd.read_csv('2_den_4_vSi.txt', sep='\s+', header=None)
data_3 = pd.read_csv('3_den_1.txt', sep='\s+', header=None)
data_4 = pd.read_csv('3_den_2.txt', sep='\s+', header=None)
data_5 = pd.read_csv('3_den_3_1.txt', sep='\s+', header=None)
data_6 = pd.read_csv('3_den_3_2.txt', sep='\s+', header=None)
data_7 = pd.read_csv('3_den_3_3.txt', sep='\s+', header=None)
# Проверяем, что в файле есть как минимум три столбца
if data.shape[1] < 3:
    raise ValueError("Файл должен содержать как минимум три столбца в каждой строке.")

# Извлекаем вторую и третью колонки (нумерация начинается с 0)
second_values = data[0].astype(float)
third_values = data[1].astype(float)
forth_values = data[2].astype(float)
second_values_1 = data_1[0].astype(float)
third_values_1 = data_1[1].astype(float)
forth_values_1 = data_1[2].astype(float)
second_values_2 = data_2[0].astype(float)
third_values_2 = data_2[1].astype(float)
forth_values_2 = data_2[2].astype(float)
second_values_3 = data_3[0].astype(float)
third_values_3 = data_3[1].astype(float)
forth_values_3 = data_3[2].astype(float)
second_values_4 = data_4[0].astype(float)
third_values_4 = data_4[1].astype(float)
forth_values_4 = data_4[2].astype(float)
second_values_5 = data_2[0].astype(float)
third_values_5 = data_2[1].astype(float)
forth_values_5 = data_2[2].astype(float)
second_values_6 = data_2[0].astype(float)
third_values_6 = data_2[1].astype(float)
forth_values_6 = data_2[2].astype(float)
second_values_7 = data_2[0].astype(float)
third_values_7 = data_2[1].astype(float)
forth_values_7 = data_2[2].astype(float)
# Строим график
# Загрузка данных из другого файла 'data_2.txt'
x2 =second_values*10
y2 =third_values
x3 =second_values_1*10
y3 =third_values_1
x4 =second_values_2*10
y4 =third_values_2
x5 =second_values_3*10
y5 =third_values_3
x6 =second_values_4*10
y6 =third_values_4
x7 =second_values_5*10
y7 =third_values_5
x8 =second_values_6*10
y8 =third_values_6
x9 =second_values_7*10
y9 =third_values_7
# Смещение данных второго графика так, чтобы он начинался со значения 4000
shift_value = 4000 - x2[0]
x2_shifted = x2 + shift_value
shift_value = 5000 - x3[0]
x3_shifted = x3 + shift_value
shift_value = 6000 - x4[0]
x4_shifted = x4 + shift_value
shift_value = 7000 - x5[0]
x5_shifted = x5 + shift_value
shift_value = 8000 - x6[0]
x6_shifted = x6 + shift_value
shift_value = 10500 - x7[0]
x7_shifted = x7 + shift_value
shift_value = 11500 - x8[0]
x8_shifted = x8 + shift_value
shift_value = 12500 - x9[0]
x9_shifted = x9 + shift_value
# Построение графиков
plt.plot(x1, y1, label='')
plt.plot(x2_shifted, y2/forth_values, label='')
plt.plot(x3_shifted, y3/forth_values_1, label='')
plt.plot(x4_shifted, y4/forth_values_2, label='')
plt.plot(x5_shifted, y5/forth_values_3, label='')
plt.plot(x6_shifted, y6/forth_values_4, label='')
plt.plot(x7_shifted, y7/forth_values_5, label='')
plt.plot(x8_shifted, y8/forth_values_6, label='')
plt.plot(x9_shifted, y9/forth_values_7, label='')
plt.ylim(1350, None)

# Отображаем график
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('')
plt.grid(True)
plt.legend()
plt.show()




