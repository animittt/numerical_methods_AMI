# implementation of the Newton-Raphson method for finding roots of equations f(x) = 0

import random
import time

def generate_random_double(a, b):
    random.seed(time.time_ns())
    return random.uniform(a, b)

def f(x):
    return x * x * x + 3 * x * x - 7

def df(x):
    return 3 * x * x + 6 * x
    
def newton_method(x0, presicion):
    iterations = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        iterations += 1
        if abs(f(x1)) < presicion or abs(x1 - x0) < presicion: # first condition ensures f(x) is close to 0, 
                                                               # second checks for significant change
            return x1, iterations
        x0 = x1

x0 = generate_random_double(1.0, 2.0)
presicion = 0.001
root, iterations = newton_method(x0, presicion)
print(f"Корень уравнения: {root.__round__(3)}")
print(f"количество итераций: {iterations}")
print(f"Значение функции в корне: {f(root).__round__(6)}")