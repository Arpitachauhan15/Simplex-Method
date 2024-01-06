import numpy as np

def get_constraint_coefficients(num_constraints, num_variables):
    coefficients = []
    for i in range(num_constraints):
        constraint_input = list(map(float, input(f"Enter coefficients for constraint {i + 1}: ").split()))
        coefficients.append(constraint_input)
    return coefficients

def simplex_maximization():
    num_variables = int(input("Enter the number of variables: "))
    num_constraints = int(input("Enter the number of constraints: "))

    c_max = list(map(float, input("Enter coefficients of the objective function to maximize: ").split()))
    A_max = get_constraint_coefficients(num_constraints, num_variables)
    b_max = list(map(float, input("Enter the right-hand side of the constraints: ").split()))

    m, n = len(A_max), len(c_max)
    tableau = np.zeros((m + 1, m + n + 1))

    tableau[:-1, :n] = np.array(A_max)
    tableau[:-1, -1] = b_max
    tableau[-1, :n] = -np.array(c_max)

    basic_vars = np.arange(n, n + m)
    non_basic_vars = np.arange(0, n)

    while np.any(tableau[-1, :n] < 0):
        pivot_col = np.argmin(tableau[-1, :n])

        if np.all(tableau[:, pivot_col] <= 0):
            print("Problem is unbounded.")
            return None

        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        pivot_row = np.argmin(ratios)

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        basic_vars[pivot_row] = pivot_col
        non_basic_vars = np.setdiff1d(non_basic_vars, pivot_col)

    optimal_solution = np.zeros(n)
    basic_indices = np.where(basic_vars < n)[0]
    optimal_solution[basic_vars[basic_indices]] = tableau[basic_indices, -1]
    
    optimal_value = tableau[-1, -1]
    
    print("\nOptimal value:", round(optimal_value, 2))
    print("Optimal solution:", optimal_solution)

# Call the function to start the optimization process
simplex_maximization()
