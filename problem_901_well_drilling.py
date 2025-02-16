import numpy as np
from scipy.optimize import minimize

# Define the expected cost function for n thresholds
l=1e10
def expected_cost(thresholds):
    n = len(thresholds)
    cost = 0
    cumulative_prob = 1
    for i in range(n):
        cost += cumulative_prob * thresholds[i]
        cumulative_prob *= np.exp(-thresholds[i])
    return cost

# Define the constraints: t1 <= t2 <= ... <= tn
def inequality_constraints(thresholds):
    return np.diff(thresholds)

# Initial guess for the thresholds
n_thresholds = 12
initial_guess = np.linspace(0.1, 3, n_thresholds)

# Perform the optimization
result = minimize(
    expected_cost, 
    initial_guess, 
    constraints={'type': 'ineq', 'fun': inequality_constraints}, 
    bounds=[(0.001, None)] * n_thresholds  # Non-negative thresholds
)

print(result)

