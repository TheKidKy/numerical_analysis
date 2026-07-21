from sympy import *

def lagrange_poly(p, l, x, y):
    """
    This functions computes the interploation of a given function using
    Lagrange polynomial method which finds a polynomial that passes through
    a given set of points. It constructs the unique polynomial of degree
    n-1 (or less) that fits n data points exactly.

    Parameters:
    - p: The symbolic variable (e.g., x = symbols('x'))
    - l: A list of Lagrange basis polynomials
    - x, y: Data points (list of x and y coordinates)

    Returns:
    - P: The Lagrange interpolation polynomial (symbolic expression)
    - L: List of Lagrange basis polynomials

    """

    n = len(x)

    if len(y) != n:
        raise ValueError("x and y must have the same length.")
    
    # Clear the list in case it already contains values
    l.clear()

    P = 0

    # Compute each Lagrange basis polynomial
    for i in range(n):
        Li = 1

        for j in range(n):
            if i != j:
                Li *= (p - x[j]) / (x[i] - x[j])

        Li = expand(i)
        l.append(Li)

        P += y[i] * Li
    
    P = expand(P)

    return P, l