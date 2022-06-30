import numpy as np
import matplotlib.pyplot as plt

x0 = 5000
y0 = 0
a = 0
b = 20
h = 0.5


def SistRK4(f, g, x0, y0, a, b, h):
    t = np.arange(a, b + h, h)
    n = len(t)
    x = np.zeros(n)
    y = np.zeros(n)

    x[0] = x0
    y[0] = y0
    print('\tx \t\t\t\t\t\t\t y')
    for i in range(n - 1):
        k1 = h * f(x[i], y[i], t[i])
        l1 = h * g(x[i], y[i], t[i])
        k2 = h * f(x[1] + k1 / 2, y[1] + l1 / 2, t[1] + h / 2)
        l2 = h * g(x[1] + k1 / 2, y[1] + l1 / 2, t[1] + h / 2)
        k3 = h * f(x[1] + k2 / 2, y[1] + l2 / 2, t[1] + h / 2)
        l3 = h * g(x[1] + k2 / 2, y[1] + l2 / 2, t[1] + h / 2)
        k4 = h * f(x[i] + k3, y[i] + l3, t[i] + h)
        l4 = h * g(x[i] + k3, y[i] + l3, t[i] + h)
        y[i + 1] = x[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + 2 * k4)
        x[i + 1] = y[i] + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + 2 * l4)
        print(x[i], '\t', y[i])
        plt.plot(t, x, t, y, 'o')
        plt.show()