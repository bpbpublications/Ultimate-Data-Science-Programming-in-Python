import scipy as myscpy
# Define the objective function
def myobjective(x):
    return x[0]**2 + 3*x[0]*x[1]

# Define the constraints
def myconstraint1(x):
    return x[0]**3 + 2*x[0]*x[1] - 200

def myconstraint2(x):
    return x[0]**2 + 2*x[0]*x[1] - 50

# Define the bounds
mybounds = [(-200, 200), (-200, 200)]

# Define the constraints dictionary
myconstraints = [{'type': 'eq', 'fun': myconstraint1},
               {'type': 'ineq', 'fun': myconstraint2}]

# Initial guess
x0 = [1, 1]

# Minimize the objective function using SLSQP method
myresult = myscpy.optimize.minimize(myobjective, x0, method='SLSQP', bounds=mybounds, constraints=myconstraints)
# Print the optimized result
print(myresult)
    