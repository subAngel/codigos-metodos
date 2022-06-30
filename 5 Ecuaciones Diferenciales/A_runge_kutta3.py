import math
import matplotlib.pyplot as plt

# Funciones
dy = lambda x, y: math.sin(x) ** 2 * y
f = lambda x: 2 * math.exp(0.5 * (x - math.sin(x) * math.cos(x)))

# Inicialización
xi = 0;
xf = 5;
h = 0.5
n = int((xf - xi) / h)
x = 0;
y = 2

# Visualizacion
print('x  \t\t y \t\t f(x)');
print('%f \t %f \t %f' % (x, y, f(x)))
x_plot = [];
y_RK3 = [];
y_analytical = []

# Metodo de RK 3er orden
for i in range(1, n + 1):
    x_plot.append(x);
    y_RK3.append(y);
    y_analytical.append(f(x))
    # Calcular aproximaciones de derivadas
    k1 = dy(x, y)
    k2 = dy(x + h / 2, y + k1 * h / 2)
    k3 = dy(x + h / 2, y - k1 * h + 2 * k2 * h)
    # Calcular nuevo valor y estimado
    y = y + 1 / 6 * (k1 + 4 * k2 + k3) * h
    x = x + h
    print('%f \t %f \t %f' % (x, y, f(x)))

# Graficación
x_plot.append(x);
y_RK3.append(y);
y_analytical.append(f(x))
plt.plot(x_plot, y_RK3, 'ro', x_plot, y_analytical)
plt.xlabel('x');
plt.ylabel('y')
plt.legend(["RK3", 'Analytical'])
