# -*- coding: utf-8 -*-
"""Punto 5 Interpolación.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18AwtsrZQ2jdBgs0qDDdL2XA-srCD1DCm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv')


x = df['X'].values
y = df['Y'].values


def divided_diff(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
            
    return coef

coef = divided_diff(x, y)

def newton_interpol(x, y, coef):
    n = len(x)
    p = coef[0][0]
    for i in range(1,n):
        term = coef[0][i]
        for j in range(i):
            term *= (x - x[j])
        p += term
    return p

p = newton_interpol(x, y, coef)

plt.plot(x, y, 'o', label='Data', color='r')
plt.plot(x, p, label='Interpolación', color='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()