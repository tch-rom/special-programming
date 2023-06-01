import math
from equations_list import equations
import inspect


def newton_method(equation, initial_guess, epsilon=0.0001, max_iterations=100):
    x = initial_guess

    for _ in range(max_iterations):
        f_x = equation(x)
        f_prime_x = (equation(x + epsilon) - f_x) / epsilon  # derivative

        if abs(f_x) < epsilon:
            return x

        x -= f_x / f_prime_x

    return None 



for eq in equations:
    equation_str = inspect.getsource(eq).strip()
    solution = newton_method(eq, 0.5)

    if solution is not None:
        print(f"{str(equation_str)} = 0 solution: x = {solution}")
    else:
        print(f"{str(equation_str)} = 0 - Max number of iterations reached")

