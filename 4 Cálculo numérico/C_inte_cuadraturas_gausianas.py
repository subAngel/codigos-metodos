import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 - x ** 2


a = 0
b = 1

x = np.array([(1 / 3) ** 0.5, -(1 / 3) ** 0.5])
w = np.array([1, 1])

u = (b - a) * x / 2 + (b + a) / 2
# Con este cambio de variable la integral queda de 1 a 1

I = (b - a) * np.sum(2 * f(u)) / 2

print(I)
