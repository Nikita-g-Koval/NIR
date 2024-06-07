import matplotlib.pyplot as plt
import numpy as np


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
    x = np.linspace(5, 15, 100) # X от -5 до 5
    # Построение прямой
    y = 5/(x+4)
    # Вывод графика
    ax.plot(x, y)
    plt.show()
