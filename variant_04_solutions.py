
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

    protocol.append((iteration, a, b, (a + b) / 2, func((a + b) / 2)))
    while (b - a) > 2 * eps:
        iteration += 1
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        protocol.append((iteration, a, b, c, func(c)))
    root = (a + b) / 2
    return root, iteration, protocol  

def save_results_to_file(filename, root, iterations, protocol):
    """
    Зберігає підсумковий корінь та відформатовану таблицю ітерацій у текстовий файл.
    """
    with open(filename, 'w+') as f:
       
        f.write("Protocol for the bisection method\n")
        f.write(f"Found root: x = {root:.6f}\n")
        f.write(f"Number of iterations: {iterations}\n")
        
        # Table header
        f.write(f"{'Iteration':<10} | {'a':<12} | {'b':<12} | {'c (midpoint)':<12} | {'f(c)':<15}\n")
        
        # Table rows
        for item in protocol:
            it, a_val, b_val, c_val, fc_val = item
            f.write(f"{it:<10} | {a_val:<12.6f} | {b_val:<12.6f} | {c_val:<12.6f} | {fc_val:<15.2e}\n")
        
    print(f"Results saved to file: {filename}")

def main():
    # Вхідні дані для Варіанту 4
    a = 0.8
    b = 1.0
    eps = 0.00003
    filename = "results_variant_04.txt"
    
    print("--- Solving the equation tan(x) - 1/x = 0 using the bisection method ---")
    print(f"Interval: [{a}, {b}]")
    print(f"Precision (eps): {eps}")
    
    try:
        # Виклик числового методу
        root, iterations, protocol = solve_bisection(target_function, a, b, eps)
        
        # Виведення результатів у консоль
        print(f"\n[Success] Root found: x = {root:.6f}")
        print(f"Number of iterations: {iterations}")
        print(f"Function value at the root: f(x) = {target_function(root):.2e}")
        
        # Виклик функції збереження у файл
        save_results_to_file(filename, root, iterations, protocol)
        
    except ValueError as e:
        print(f"[Error]: {e}")
