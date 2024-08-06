import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файлов
# Предполагается, что каждый файл имеет две колонки: x и y
data = np.loadtxt('pres.txt', delimiter=';')  # Файл с данными x и y1
data1 = np.loadtxt('200s_data.txt', delimiter=';')  # Файл с данными x и y1
data2 = np.loadtxt('200s_V_I.txt', delimiter=';')  # Файл с данными x и y2
print(data)
# Извлечение оси x и значений y1 и y2
x = data
y1 = data1[:, 0]
y2 = data2[:, 1]

# Построение графика зависимости y2 от y1
plt.semilogx(x*100, y1, marker='o', linestyle='-')
plt.xlabel('P, Па')
plt.ylabel('U, В ')
plt.title('График зависимости P от U, промышленный')
plt.grid(True)
plt.show()
