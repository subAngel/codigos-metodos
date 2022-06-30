import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Definimos f de x
def f(x) :
    return 1-x**2
a=10
b=45

N=9
x=np.linspace(a,b,N)
dx=(b-a)/(N-1)
y=f(x)
#Integracion
I=integrate.simps(y,x)
#
print(I)