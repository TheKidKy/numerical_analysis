def false_position(f, a, b, tol=1e-6, max_iter=100):
    """
    This function solves for f(x) = 0 using the false position method.

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
    
    for _ in range(max_iter):
        x = b - f(b) * (b - a) / (f(b) - f(a))
        if abs(f(x)) < tol:
            return x
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    raise ValueError("Maximum iterations exceeded.")