from sympy import Symbol #Manipular las expreciones de forma algebraica
from scipy.misc import derivative
x=Symbol('x')    #x
y=2*x**3        #ponemos nuestra expresion
derivada= y.diff(x)  #Derivanos  respecto a x
print(derivada)   #imprimimos la derivada
f=lambda x: 2*x**3  #Calculamos derivada númerica
print(derivative(f,1.0,dx= 1e-8))
