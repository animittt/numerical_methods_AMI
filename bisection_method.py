#метод половинного деления 
import math

def bisection_method(f, a, b, eps = 0.001):
  while True:
    c = (a+b)/2
    if abs(f(c)) < eps or (b-a)/2 < eps:
      return c
    if f(a) * f(c) < 0:
      b = c
    else:
      a = c

f = lambda x: math.cos(x) - x
print(bisection_method(f, 0, 1))