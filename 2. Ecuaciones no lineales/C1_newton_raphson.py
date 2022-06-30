# Método de Newton-Raphson de una variable

import numpy as np

# INGRESO
fx  = lambda x: x**3 + 4*(x**2) - 10 # ESTA ES LA EXPRESIÓN
dfx = lambda x: 3*(x**2) + 8*x		# ESTA ES LA EXPRESIÓN DE LA DERIVADA

x0 = 2		# Extremo derecho del intervalo
tolera = 0.001	# Tolerancia

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tramo)

