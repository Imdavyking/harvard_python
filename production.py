# 50x + 80y

# 5x + 2y <= 20

# 10x + 12y >= 90 -> -10x - 12y <= -90

import scipy
import scipy.optimize

result = scipy.optimize.linprog(
    [50,80], # Cost function 50x + 80y
    A_ub=[[5,2],[-10,-12]], # Coefficients for inequalities
    b_ub=[20,-90], # Constants for inequalities
)

if result.success:
    print(f"X1: {round(result.x[0],2)} hours")
    print(f"X2: {round(result.x[1],2)} hours")
else:
    print("No solution")