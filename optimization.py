# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:41:57 2016

@author: Joanne
"""

import scipy.optimize as sp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3.0,3.0,0.1)

def f(x):
    return -np.exp(-(x - .7)**2)

x0=0

bnds=[(0,0.5)]

res= sp.minimize(f, x0)

print res
plt.scatter(x, f(x))
plt.scatter(res['x'], f(res['x']), color='red')