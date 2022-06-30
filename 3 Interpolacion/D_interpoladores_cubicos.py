
# SPLINE CÚBICO
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def CubicNatural(xi, yi):
    m = xi.size
    n = m-1
    a = np.zeros(m)
    b = np.zeros(n)
    c = np.zeros(m)
    d = np.zeros(n)
    for i in range(m):
        a[i] = yi[i]
    h = np.zeros(n)
    for i in range(n):
        h[i] = xi[i+1] - xi[i]
    alfa = np.zeros(n)
    alfa[0] = 0
    for i in range (1,n):
        alfa[i] = 3*(a[i+1]-a[i])/h[i]-3*(a[i]-a[i-1])/h[i-1]
    l=np.zeros(m)
    z=np.zeros(m)
    u=np.zeros(n)
    l[0] = 1
    z[0] = 0
    u[0] = 0
    for i in range(1,n):
        l[i] = 2*(xi[i+1]-xi[i-1])-h[i-1]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (alfa[i]-h[i-1]*z[i-1])/l[i]
    l[m-1] = 1
    z[m-1] = 0
    c[m-1] = 0
    for i in np.flip(np.arange(n)):
        c[i] = z[i]-u[i]*c[i+1]
        b[i] = (a[i+1]-a[i])/h[i]-h[i]*(c[i+1]+2*c[i])/3
        d[i] = (c[i+1]-c[i])/(3*h[i])

    x = sym.Symbol('x')
    px_tabla = []
    for j in range(0,n,1):

        pxtramo = d[j] * (x-xi[j])**3 + c[j]*(x-xi[j])**2
        pxtramo = pxtramo + b[j]*(x-xi[j])+ a[j]

        px_tabla.append(pxtramo)
    return a, b, c, d,px_tabla

x1 = np.linspace(0, 1.5, 600)
xi = np.array([0,0.5,1,1.5])
f = lambda x: np.cos(3*x**2)*np.log(x**3+1)
fi = f(xi)
f1 = f(x1)
muestras = 10
n = len(xi)
a,b,c,d,px_tabla = CubicNatural(xi,fi)

print('Polinomios por tramos: ')
for tramo in range(1,n,1):
    print('x = ['+str(xi[tramo-1])+','+str(xi[tramo])+']')
    print(str(px_tabla[tramo-1]))
