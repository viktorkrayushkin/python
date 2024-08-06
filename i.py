import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла 'data.txt'
data = np.loadtxt('200s_data.txt', delimiter=';')
# Разделение данных на x и y
x = data[:, 0]
y = data[:, 1]

# Построение графика
plt.plot(x, y)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('График из данных data.txt')
plt.grid(True)
plt.show()
