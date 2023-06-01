import math
from autograd import grad
import autograd.numpy as np
functions = [
        lambda x,y: (1.5 - x + x * y) ** 2 + (2.25 - x +
            x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2,
        lambda x,y: (1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x * x - 14 * y + 6 * x * y + 3 * y * y)) * (30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x * x + 48 * y - 36 * x * y + 27 * y * y)), 
        lambda x,y: 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y,
        lambda x,y: (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2,
        lambda x,y: 2 * x * x - 1.05 * x ** 4 + x ** 6 / 6 + x * y + y * y,
        lambda x,y: np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y,
        lambda x,y: 200 * np.exp(-0.02 * np.sqrt(x*x + y*y)) + 5 * np.exp(np.cos(3 * x) + np.sin(3 * y)),
        lambda x,y: np.cos(x)*np.sin(y) - x / (y * y + 1),
        lambda x,y: abs(x * x + y * y + x * y) + abs(np.sin(x)) + abs(np.cos(y)),
        lambda x,y: np.sin(x) * np.exp((1 - np.cos(y)) ** 2) + np.cos(y) * np.exp((1 - np.cos(x)) ** 2) + (x - y) ** 2,
        lambda x,y: (x + 10) ** 2 + (y + 10) ** 2 + np.exp(-x**2 - y ** 2),
        lambda x,y: x*x + 2* y*y - 0.3 * np.cos(3 * math.pi * x) * 0.4 * np.cos(4 * math.pi * y) + 0.3,
        lambda x,y: x * x + 2 * y * y - 0.3 * np.cos(3 * math.pi * x + 4 * math.pi * y) + 0.3,
        lambda x,y: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2
    ]

