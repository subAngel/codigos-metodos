#Primero tenemos que importar las librerias
import numpy as np
from numpy.polynomial import polynomial as P

# y ponemos la coordenada en x
x = np.linspace(-1,1,51)

# Mostramos la coordenada
print("X Coordenada...\n",x)

# y ponemos la coordenada en y
y = x**3 - x + np.random.randn(len(x))
print("\nY Coordenada...\n",y)


# usamos polynomial.polyfit() en Python Numpy para optener el ajuste polinomial
c, stats = P.polyfit(x,y,3,full=True)
print("\nResultado...\n",c)
print("\nResultado...\n",stats)
