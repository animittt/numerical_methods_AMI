# Метод простых итераций для нахождения корня уравнения f(x) = 0
# подаем коду x=g(x), где g(x) - функция, либо прямо полученная из уравнения, либо имеет вид x - f(x)/alpha
# где |alpha|  > max|f'(x)|/2 на рассматриваемом отрезке а sgn alpha = sgn f'(x) на этом отрезке
#g(x) сжимающее отображение на рассматриваемом отрезке, т.е. |g'(x)| <= q,  на этом отрезке, |g(x) - g(y)| < q*|x-y|, 0<q<1
# но для использования второго варианта подбора g(x), надо чтобю f'(x) имела постоянный знак на этом отрезке
import random
import time

def generate_random_double(a, b):
    random.seed(time.time())
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