#метод секущих для x * x * x + x * x - 5 = 0, presicion = 0.001
def f(x):
    return x * x * x + x * x - 5

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
x0 = 1.0
x1 = 2.0
presicion = 0.001
root = secant_method(x0, x1, presicion)
print(f"Корень уравнения: {root}")