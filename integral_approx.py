import numpy as np

def left_rectangle_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a, b - h, n)
  return h * np.sum(f(x))

def right_rectangle_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a + h, b, n)
  return h * np.sum(f(x))

def midpoint_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a + h / 2, b - h / 2, n)
  return h * np.sum(f(x))

def trapezoidal_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a, b, n+1)
  return (h/2) * (f(x[0]) + f(x[-1]) + 2*np.sum(f(x[1:-1])))

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return (h / 3) * (f(x[0]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-2:2])) + f(x[-1]))

def f(x):
    return np.exp(-x**2)

def f_derivative(x):
  return -2*x * np.exp(-x**2)

def f_2nd_derivative(x):
  return np.exp(-x**2) * (4*x**2 - 2)

def f_4th_derivative(x):
  return np.exp(-x**2) * (16*x**4 - 48*x**2 + 12)

M1 = max(abs(f_derivative(np.linspace(0, 1, 1000))))
M4 = max(abs(f_4th_derivative(np.linspace(0, 1, 1000))))
M2 = max(abs(f_2nd_derivative(np.linspace(0, 1, 1000))))

epsilon = 1e-4
a, b = 0, 1

n_trapez = int(np.sqrt( ((b-a)**3 * M2) / (12 * epsilon))) + 1 # n for trapezoidal
n_simpson = int( (( (b-a)**5 * M4) / (180 * epsilon) )**0.25 ) + 1  # n for simpson
n_left = int( (( (b-a)**2 * M1) / (2 * epsilon) ) + 1 )  # n for left rectangle
n_right = n_left  # n for right rectangle
n_midpoint = n_left  # n for midpoint

value_trapezoid = trapezoidal_rule(f, a, b, n_trapez)
value_simpson = simpsons_rule(f, a, b, n_simpson)
value_left = left_rectangle_rule(f, a, b, n_left)
value_right = right_rectangle_rule(f, a, b, n_right)
value_midpoint = midpoint_rule(f, a, b, n_midpoint)

print("Required n = ", n_trapez)
print("Integration value I = ", value_trapezoid)
print("Required n for Simpson = ", n_simpson)
print("Integration value I for Simpson = ", value_simpson)
print("Required n for Left Rectangle = ", n_left)
print("Integration value I for Left Rectangle = ", value_left)
print("Required n for Right Rectangle = ", n_right)
print("Integration value I for Right Rectangle = ", value_right)
print("Required n for Midpoint = ", n_midpoint)
print("Integration value I for Midpoint = ", value_midpoint)