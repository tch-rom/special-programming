import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

def parse_file(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split('\t')
            x.append(float(values[0].replace(',', '.')))
            y.append(float(values[1].replace(',', '.')))
    return x, y

def polynomial_function(x, *coeffs):
    return np.polyval(coeffs, x)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No data file. Usage: python graph_data.py filename")
        sys.exit(1)

    filename = sys.argv[1]
    x, y = parse_file(filename)

    # Побудова полінома певного ступеня
    degree = 3

    # Визначення початкових наближень для коефіцієнтів полінома
    initial_guess = np.zeros(degree + 1)

    coeffs, _ = curve_fit(polynomial_function, x, y, p0=initial_guess)

    # Побудова функції апроксимації
    approx_func = lambda x: polynomial_function(x, *coeffs)

    # Виведення результатів
    print("Для файлу", filename)
    print("Коефіцієнти полінома:", coeffs)

    # Побудова графіку
    plt.scatter(x, y, label='Дані')
    plt.plot(x, approx_func(x), color='red', label='Апроксимація')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

