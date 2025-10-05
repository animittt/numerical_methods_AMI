# Метод простых итераций для нахождения корня уравнения f(x) = 0

import random
import time

def generate_random_double(a, b):
    random.seed(time.time_ns())
    return random.uniform(a, b)


def f(x):
    return x * x * x + 3 * x * x - 7

def simple_iteration_method(x0, presicion):
    while True:
        x1 = x0 - f(x0) / 13.0
        if abs(f(x1)) < presicion:
            return x1
        x0 = x1

# пример использования
x0 = generate_random_double(1.0, 2.0)
presicion = 0.001
root = simple_iteration_method(x0, presicion)
print(f"Корень уравнения: {root.__round__(3)}")