#метод секущих  для нахождения корня уравнения f(x) = 0
# x0,x1 - начальные приближения берем такими, что f(x0) и f(x1) имеют разные знаки, и f(x0)f''(x0)>0
# def f(x):
#     return x * x * x + x * x - 5
import math

def secant_method(x0, x1, presicion):
    if abs(f(x0)) < presicion:
        return x0
    if abs(f(x1)) < presicion:
        return x1
    if abs(f(x1) - f(x0)) < 1e-12:  # предотвращение деления на ноль
        raise ValueError("f(x1) и f(x0) слишком близки друг к другу.")
    
    while True:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(f(x2)) < presicion:
            return x2
        x0, x1 = x1, x2


# пример использования
f = lambda x: math.cos(x) - x
x0 = 0
x1 = 1
presicion = 0.001
root = secant_method(x0, x1, presicion)
print(f"Корень уравнения: {root}")