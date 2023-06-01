from autograd import grad
from objective_functions import functions


def minimize_function(func, x, y, tolerance):
    alpha = 0.001  # Learning rate
#    max_iterations = 1000
    iteration = 0
    grad_norm = float('inf')
    df_dx = grad(func, argnum=0)
    df_dy = grad(func, argnum=1)
    
    while grad_norm > tolerance and iteration < max_iterations:
        
        grad_x = df_dx(x, y)
        grad_y = df_dy(x, y)
        
        x -= alpha * grad_x
        y -= alpha * grad_y
        grad_norm = (grad_x ** 2 + grad_y ** 2) ** 0.5
        iteration += 1

    return x, y

# Define max of iterations 
max_iterations = 1000

# Initial point
x_initial = 0.1
y_initial = 0.1

# Tolerance
tolerance = 1e-6

for func in functions:
# Minimize the objective function
    x_min, y_min = minimize_function(func, x_initial, y_initial, tolerance)

# Print the result
    print(f"Minimum of the objective function: x = {x_min}, y = {y_min}")

