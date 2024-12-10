def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    This function solves f(x) = 0 using the bisection method.

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
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")

    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        midpoint = (a + b) / 2
        f_mid = f(midpoint)

        if f_mid == 0:  # Found the root
            return midpoint, iterations

        if f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

        iterations += 1

    root = (a + b) / 2
    return root, iterations