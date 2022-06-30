import numpy as np
import matplotlib.pyplot as plt
#Definicion de la funcion f de x
def f(x) :
    return 3*x**3+2*x**2+5*x+1
N=10
a=-2
b=2
#Vector de x que va de a - b y toma N datos
x=np.linspace(a,b,N)
dx=(b-a)/(N-1)
y=f(x)
#Llena de ceros el arreglo
yp=np.zeros_like(x)
#Condicion del rango que tiene N
for i in range(N) :
    if i==0:
        yp[i]=(y[i+1]-y[i])/dx
    elif i==N-1:

        yp[i]=(y[i]-y[i-1])/dx
    else:
        yp[i]=(y[i+1]-y[i-1])/(2*dx)
#Definición de la funcion fp de x
def fp(x):
    return 9*x**2+4*x+5
#Creacion de la grafica
plt.plot(x,fp(x),
'g-')
plt.plot(x,yp,"bo")
plt. show()

