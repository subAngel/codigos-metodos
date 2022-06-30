# METODO DE NEWTON-RAPHON DE VARIAS VARIABLES

import numpy as np
#Definicion de la funcion en el vector x
def F(x) :
    f1=x[0]**2+x[1]**2-1
    f2=4*x[0]**2/9+4*x[1]**2-1
    return np.array([f1,f2])
#Definicion de la derivada de la funcion
def dF(x):
    return np.array([[2*x[0],2*x[1]],
                     [8*x[0]/9,8*x[1]]])
N=100
x=np.array([1,1])
#Iteracion de newton-raphson
for k in range(N) :
    xold=x
    Jinv=np.linalg.inv(dF(x))
    x=x-np.dot(Jinv,F(x))
    e=np.linalg.norm(x-xold)
    print(k,x,e)
    if e<1e-10:
        break
