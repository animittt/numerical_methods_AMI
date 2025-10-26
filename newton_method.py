# implementation of the Newton method for finding roots of equations f(x) = 0
"""
корень уравнения изолирован на отрезке [а,b], f(a)*f(b)<0
f'(x) и f''(x) имеют постоянный знак на этом отрезке (т.е. функция монотонна и вогнута или выпукла)
начальное приближение x0 выбирается в зависимости от знаков f(a), f(b) и f''(x) на отрезке: 
если f(a) и f(b) имеют разные знаки, то x0 = a или x0 = b, в зависимости от знака f''(x).
Если f(a)*f''(a)>0, то x0 = a, иначе x0 = b
условие фурье для сходимости метода: f(x0)*f''(x0) > 0
"""
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