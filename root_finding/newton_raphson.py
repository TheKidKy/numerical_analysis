from sympy import *

def newton_raphson(f, a, b, tol=1e-6, max_iter=100):
    """
    This function solves f(x) = 0 using the newton-raphson method.

    Parameters:
    - f: Function for which we are finding the root
    - a: Start of interval [a, b]
    - b: End of interval [a, b]
    - tol: Tolerance for the solution (default: 1e-6)
    - max_iter: Maximum number of iterations (default: 100)

    Returns:
    - root: Approximated root of the function
    - iterations: Number of iterations performed
    """

    x = symbols('x')

    # initial guess -> midpoint of the interval
    current = (a + b) / 2
    
    derivative = diff(f, x)

    # convert symbolic expressions to numerical functions
    f_num = lambdify(x, f, "math")
    df_num = lambdify(x, derivative, "math")

    for i in range(max_iter):
        fx = f_num(current)
        dfx = df_num(current)

        # Prevent division by zero
        if abs(dfx) < 1e-12:
            raise ValueError("Derivative is zero. Newton-Raphson cannot continue.")
        
        next_x = current - fx / dfx

        # Check convergence
        if abs(next_x - current) < tol:
            return next_x, i + 1
        
        current = next_x

    raise ValueError("Method did not converge within the maximum number of iterations.")
    

