from initial_points import initials

def rosenbrock(x, y):
    return (1 - x)**2 + 100*(y - x**2)**2

def gradient(x, y):
    dx = -2*(1 - x) - 400*x*(y - x**2)
    dy = 200*(y - x**2)
    return dx, dy

def minimize_rosenbrock(x, y, tolerance):
    alpha = 0.0001  # Learning rate
    max_iterations = 100
    iteration = 0
    grad_norm = float('inf')

    while grad_norm > tolerance and iteration < max_iterations:
        grad_x, grad_y = gradient(x, y)
        x -= alpha * grad_x
        y -= alpha * grad_y
        grad_norm = (grad_x**2 + grad_y**2)**0.5
        iteration += 1

    return x, y


# Tolerance
tolerance = 1e-3

# Initial points
for init in initials:
    x_initial = init[0]
    y_initial = init[1]

# Minimize the Rosenbrock function
    x_min, y_min = minimize_rosenbrock(x_initial, y_initial, tolerance)

# Print the result
    print(f"{x_initial, y_initial}\tMin of the Rosenbrock func: x = {x_min}, y = {y_min}")

