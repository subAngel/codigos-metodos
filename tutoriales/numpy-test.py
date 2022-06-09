import numpy as np
from numpy.linalg import solve, inv

a = np.array([[-1,1,2.5],[1.3, 4.2]])    # Matriz forma (2,2)
print(a)
print(a.T)      # transpuesta
print(inv(a))   # inversa

b = np.array([[2],[-3]])    # vector forma (2,1)
print(b)
s = solve(a,2)  # solucionar sistema de ecuaciones
print(s)


