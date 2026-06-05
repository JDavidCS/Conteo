def factorial(n: int):
    """
    Factorial con ciclo for
    """
    p = 1
    for i in range(n):
        p *= (n-i)
    return p
def r_factorial(n: int):
    """
    Factorial con recursividad
    """
    if n <= 1:
        return 1
    return n*r_factorial(n-1)
def div_factorial(n:int, k:int):
    """
    n!/k!
    """
    if n < k or n < 1 or n < 1: return -1 # n tiene que ser mayor a k y ambos positivos 
    if n == k: return 1 # igual a decir n!/n!}
    return _dec_factorial(n,k)
def _dec_factorial(n:int, k:int):
    if n<=k: return 1
    return n*_dec_factorial(n-1,k)