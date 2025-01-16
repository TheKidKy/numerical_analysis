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

    init = (a + b) / 2
    x = symbols('x')
    derivative = diff(f, x)

    

