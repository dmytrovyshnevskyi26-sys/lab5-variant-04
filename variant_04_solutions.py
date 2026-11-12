
"""
Лабораторна робота №5
Функції та декомпозиція задач
Вишневський Дмитро
EIP30
"""
import math
def target_function(x):
    """
    Цільова функція
    """
    return math.tan(x) - 1/x


def solve_bisection(func, a, b, eps):
    """
    Реалізує метод ділення навпіл.
    Приймає математичну функцію як аргумент, межі [a, b] та точність eps.
    Повертає: корінь, кількість ітерацій, список-протокол обчислень.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Функція повинна мати різні знаки на кінцях відрізка [a, b].")
    iteration = 0
    protocol = []

    protocol.append(f"iteration {iteration}: a = {a}, b = {b}, c = {(a + b) / 2}, f(a) = {func(a)}, f(b) = {func(b)}, f(c) = {func((a + b) / 2)}")

    while (b - a) > 2 * eps:
        iteration += 1
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        protocol.append(f"iteration {iteration}: a = {a}, b = {b}, c = {c}, f(a) = {func(a)}, f(b) = {func(b)}, f(c) = {func(c)}")
    root = (a + b) / 2
    return root, iteration, protocol  
