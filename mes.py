import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файлов
# Предполагается, что каждый файл имеет две колонки: x и y
data1 = np.loadtxt('Default Dataset.txt', delimiter=',')  # Файл с данными x и y1


# Извлечение оси x и значений y1 и y2
x = data1[:, 0]
y = data1[:, 1]
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

# Применение сглаживания
window_size = 5
smoothed_y = moving_average(y, window_size)

# Построение графика зависимости y2 от y1
plt.plot(x[:len(smoothed_y)], smoothed_y, label='Сглаженные данные (скользящее среднее)', color='green')
plt.xlabel('t, c')
plt.ylabel('E_x, В')

plt.title('График зависимости t от E_x')
plt.grid(True)
plt.show()


# Функция для скользящего среднего


# Построение графиков



