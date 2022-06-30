import numpy as np
import matplotlib.pyplot as plt

# Funcion:  x'(t)=4*x(t)/t, x(1)=1
t0 = 1  # valor inicial de t
tn = 2  # valor final de t
x0 = 1  # valor inicial de x
n = 20  # numero de pasos


def EulerI(t0, tn, x0, n):
    t = np.linspace(t0, tn, n + 1)
    x = np.zeros(n + 1)
    x[0] = x0
    h = (tn - t0) / n  # Tamaño de paso

    # Euler
    for i in range(1, n + 1):
        x[i] = x[i - 1] * (t[i - 1] + h) / (t[i - 1] - 3 * h)
        print(t[i], "\t", format(x[i], '6f'))  # Visualizacion de resultados
    return t, x


# Grafico
(t, x1) = EulerI(t0, tn, x0, n)
plt.plot(t, x1)