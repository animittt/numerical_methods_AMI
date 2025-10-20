#interpolation
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = np.linspace(0,3.2,17)
y = np.array([1,0.98,0.92,0.83,0.7,0.54,0.36,0.17,-0.03,-0.23,-0.42,-0.59,-0.74,-0.86,-0.94,-0.99,-0.99])
z = sp.Symbol('z')

def interpolation(x, y, z):
  sum = 0
  for i in range(len(x)):
    f = y[i]
    for k in range(len(x)):
      if k==i:
        continue
      f *= (z-x[k])/(x[i]-x[k])
    sum += f
  return sum

result = sp.simplify(interpolation(x, y, z))

plt.plot(x,y,color='red')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

A = sp.lambdify(z, result, 'numpy')
xres = np.linspace(0, 3.2, 2000)
yres = A(xres)
plt.plot(xres, yres)
plt.show()