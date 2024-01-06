from scipy.optimize import linprog

def solve_linear_program(c, A_eq=None, b_eq=None, A_ub=None, b_ub=None, minimize=True):
    # Convert maximization problem to minimization if needed
    if not minimize:
        c = [-x for x in c]

    bounds = [(0, None) for _ in range(len(c))]  # xi >= 0 for all variables

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='simplex')

    # Convert the result back for maximization problems
    if not minimize:
        result.fun = -result.fun

    return result.x, result.fun


# Example problem for maximization:
# Maximize Z = x1-x2+3x3
# Subject to:
#   x1 + x2 + 0x3 <= 20
#   x1 + 0x2 + x3 =5
#   0x1 + x2 + x3 >= 10
#   x1, x2, x3 >= 0

c_max = [1, -1, 3]  
A_eq_max = [[1, 0, 1]]
b_eq_max = [5]
A_ub_max = [[1, 1, 0], [0, -1, -1]]
b_ub_max = [20, -10]

solution_max , optimal_value_max = solve_linear_program(c_max , A_eq=A_eq_max , b_eq=b_eq_max , A_ub=A_ub_max , b_ub=b_ub_max , minimize=False)

print("Optimal Solution for Maximization:", solution_max )
print("Optimal Objective Value (Z) for Maximization:", optimal_value_max )

#minimization prblm
# minimize 12x1 + 20x2
#constraint
# 6x1 + 8x2 >= 100
# 7x1 + 12x2 >= 120

c_min=[12, 20]
A_ub_min=[[-6, -8], [-7, -12]]
b_ub_min=[-100, -120]

sol_min, opti_min= solve_linear_program(c_min, A_eq=None, b_eq=None, A_ub=A_ub_min, b_ub=b_ub_min, minimize=True)
print("optimal sol:", sol_min)
print("optimal value:")
print(opti_min)
