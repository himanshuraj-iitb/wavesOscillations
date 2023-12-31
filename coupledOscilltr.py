# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11tFEs0mlWuLILonAglBb1inB9H1Dq5LL
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib

k = 1
m = 1          #mass of either blocks
dt = 0.0001      #time step
t_end = 100                         #total time duration
nx = 101                           #grid points
x = np.linspace(0,1,nx)
N = int(t_end/dt)                   # number of time grid points
t = np.linspace(0,t_end,N)     #time slices
w1 = math.sqrt(k/m)
w2 = math.sqrt(3*k/m)

A = np.array([[0,0,1,0],[0,0,0,1],[-2*k/m, k/m, 0,0],[k/m,-2*k/m,0,0]])           # matrix formulation

# Analytical sol
x1 = 0.5*(np.cos(w1*t) + np.cos(w2*t))
x2 = 0.5*(np.cos(w1*t) - np.cos(w2*t))
X = np.array([x1,x2])

x0 = [0,0,1,0]   #initial condition (x1 = 1, x2 = 0, v1 = 0, v2 = 0)

#forward euler scheme
xF = np.zeros((4,N))
xF[:,0] = x0      #setting up the initial conditions
for k in range(N-1):
  xF[:,k+1] = np.dot((np.eye(4) + dt*A),xF[:,k])

plt.plot(t,x1,'k')
plt.plot(t,x2,'r')
plt.xlim(0,50)
plt.ylim(-2,2)

plt.grid('True')
plt.plot(t,xF[2,:],'b--',linewidth = '1.2')
plt.plot(t,xF[3,:],'g--',linewidth = '1.2')
plt.plot(t,x1,'r-',linewidth = '0.2')
plt.plot(t,x2,'k-',linewidth = '0.2')
plt.xlim(0,50)
plt.ylim(-2,2)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title("Coupled Harmonic Oscillator")
plt.legend(["x1_numerical", "x2_numerical","x1_analytical","x2_analytical"], loc ="lower right")
print(xF)