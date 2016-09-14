# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:06:16 2016

@author: Joanne
"""

import HBV96
import numpy as np
import matplotlib.pyplot as plt

#import data from file
data = np.loadtxt('BrueDataAll.csv', skiprows=1, delimiter=',')
rt = data[:, 0]
et = data[:,1]
qt = data[:, 3]

#set temperature and non-calibration parameters p2[timestepFactor, area]
temp = -20.0*np.ones_like(rt)
p2=[1.0, 135.0]

#run calibration
par, nse = HBV96.calibrate(qt, rt, temp, et, p2, verbose='TRUE', obj_fun='NSE')

#run simulation for calibrated parameters
q, st = HBV96.simulate(rt, temp, et, par, p2)

#display results
plt.plot(q)
plt.plot(qt)

print par, -nse