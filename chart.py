import matplotlib.pyplot as plt
import numpy as np
import math


def show_chart():
    # Создаём экземпляр класса figure и добавляем к Figure область Axes
    fig, ax = plt.subplots()
    # Добавим заголовок графика
    ax.set_title('График функции')
    # Название оси X:
    ax.set_xlabel('x')
    # Название оси Y:
    ax.set_ylabel('y')
    # Начало и конец изменения значения X, разбитое на 100 точек
    x = np.linspace(0.1, 0.8, 100)
    # Построение прямой
    y = [math.sin(val) - math.cos(val) for val in x]
    # Вывод графика
    ax.plot(x, y)
    plt.show()
