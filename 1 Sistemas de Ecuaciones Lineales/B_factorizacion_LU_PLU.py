import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import scipy.linalg as la
import nimfa
from sklearn.decomposition import NMF, PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pandas as pd

## FACTORIZACIÓN LU
# graficos incrustados
%matplotlib inline

# parámetros de estilo
sns.set(style='darkgrid', palette='muted')
pd.set_option('display.mpl_style', 'default')
pd.set_option('display.notebook_repr_html', True)
plt.rcParams['figure.figsize'] = 8, 6


# FACTORIZACIÓN PLU
m=int (input ("Introduce el número de renglones"))
matriz=np.zeros([m,m])
u=np.zeros([m,m])
l=np.zeros([m,m])
print ("Introduce los elementos de la matriz")
for r in range(0, m) :
    for c in range(0, m) :
        matriz[r, c]= (input ("ELmento a[" +str(r+1)+","+str(c+1)+"]"))
        matriz[r,c]=float(matriz[r,c])
        u[r,c]= matriz [r,c]

for k in range(0, m) :
    for r in range (0,m) :
            if (k==r) :
                l[k,r]=1
            if (k<r) :
                factor=(matriz[r,k]/matriz[k,k])
                l[r,k]=factor
                for c in range(0, m) :
                    matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                    u[r,c]=matriz[r,c]

print ("Impresión de resultados")
print(l)
print(u)
