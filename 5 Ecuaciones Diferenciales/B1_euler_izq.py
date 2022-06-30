import numpy as np
import matplotlib.pyplot as plt

# d/dt=-U1
# du1/dt= (-g/l)*sin theta

# Datos
m = 1
l = 1
g = 9.8

# Condiciones Iniciales
t = 0
x1 = 0
y1 = 0.5
u = np.array([x1, y1])


# Sistema de ecuaciones
def f(u, t):
    return np.array([u[1], -g * np.sin(u[0]) / l])


tsol = [t]
xsol = [u[0]]
ysol = [u[1]]
dt = 0.25
tfin = 10
print('t\t\tx\t\t\t\t\ty')
while t < tfin:
    u += f(u, t) * dt
    t += dt
    xsol.append(u[0])
    ysol.append(u[1])
    tsol.append(t)
    print(t, '\t', u[0], '\t', u[1])

plt.plot(tsol, xsol)
plt.plot(tsol, ysol)
plt.show()