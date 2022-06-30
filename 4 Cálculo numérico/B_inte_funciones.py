from sympy import Symbol #importamos las librerias
from sympy import integrate#Es la parte que me va hacer la integral de forma simbolica

from scipy.integrate import quad
x=Symbol('x') #X va ser igual a un Simbolo
print(integrate(x**3+x**2+1,x))  #vamos a imprimir el resultado de la integral que necesitamos integral
                                 #el ** significa una potencia
                                 #después la variable a la que se va a integrar que es la x
f=lambda x:x**3+x**2+1           #crear funciones anonimas
print(quad(f,1,2))                #integrales de forma númerica
