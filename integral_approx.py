import numpy as np

def left_rectangle_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b - h, n)
    return h * np.sum(f(x))

def right_rectangle_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h, b, n)
    return h * np.sum(f(x))


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return (h / 2) * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(x))

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return (h / 3) * (f(x[0]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-2:2])) + f(x[-1]))

def f(x):
    return np.exp(-x**2)

def f2(x):
    return np.exp(-x**2) * (4 * x**2 - 2)

M2 = max(abs(f2(np.linspace(0, 1, 1000))))
epsilon = 1e-4
a, b = 0.0, 1.0
n = int(np.sqrt(( (b - a)**3 * M2 ) / (12 * epsilon))) + 1

print("Estimated n for Simpson's Rule:", n)
print("Left Rectangle Rule:", left_rectangle_rule(f, a, b, n))
print("Right Rectangle Rule:", right_rectangle_rule(f, a, b, n))
print("Trapezoidal Rule:", trapezoidal_rule(f, a, b, n))
print("Midpoint Rule:", midpoint_rule(f, a, b, n))
print("Simpson's Rule:", simpsons_rule(f, a, b, n))