import numpy as np

def euler_method(f, x0, y0, h, a, b):
    n = int((b - a) / h)
    x_values = np.linspace(x0, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for i in range(1, n + 1):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])

    return x_values, y_values

def f(x, y):
    return x**2 - y**2

x0 = 0
y0 = 0
h = 0.2
a = 0
b = 1

x_values, y_values = euler_method(f, x0, y0, h, a, b)
for x, y in zip(x_values, y_values):
    print(f"x: {x:.2f}, y: {y:.6f}")

