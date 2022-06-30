import numpy as np
from matplotlib import pyplot as plt

# Funcion:  y'=4*y/x, y(0)=1

x0 = 1  # Condicion inicial de x
y0 = 1  # Condicion inicial de y
xf = 2  # Valor final
n = 21  # numero de pasos
h = (xf - x0) / (n - 1)  # tamaño de paso
x = np.linspace(x0, xf, n)


def f(x, y):
    return 4 * y / x  # Funcion


y = np.zeros([n])  # Vector de y
y[0] = y0

# Euler
for i in range(1, n):
    y[i] = y0 + h * f(x[i], y0)
    y0 = y[i]

# Visualizacion de resultados
print("x\t\t    y")
for i in range(n):
    print(x[i], "\t", format(y[i], '6f'))

# Grafica
plt.plot(x, y)
plt.xlabel("Valor de x")
plt.ylabel("Valor de y")
plt.title("Aproximacion de la Solucion con el metodo de Euler")
plt.show()
