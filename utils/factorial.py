
def factorial(n: int):
    """
    Factorial con ciclo for
    """
    p = 1
    for i in range(n):
        p *= (n-i)
    return p
def r_factorial(n):
    """
    Factorial con recursividad
    """
    if n <= 1:
        return 1
    return n*r_factorial(n-1)