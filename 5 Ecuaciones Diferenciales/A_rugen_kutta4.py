from math import *


def f(t, y):
    func = t * exp(3 * t) - 2 * y
    return func


def RK4(t, y, h, n):
    print('y(', t, ')=', y)
    for k in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + (h / 2) * k1)
        k3 = f(t + h / 2, y + (h / 2) * k2)
        k4 = f(t + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h
        print('y(', t, ')=', y)


RK4(0, 2, 0.25, 4)
