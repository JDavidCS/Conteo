"""
Por la forma: n!/r!(n-r)! en vez de calcular todos los fatoriales
mejor se cancela n! con el factorial más grande del denominador.
"""
from utils.factorial import *
def combinacion(n:int, r:int):
    """
    n -> Cantidad elementos
    r -> tamaño del grupo
    return -1 en caso de error
    """
    if r<n: return -1       # solo datos validos
    if n-r>r:
        return div_factorial(n,(n-r))//r_factorial(r)
    else:
        return div_factorial(n,r)//r_factorial(n-r)
def combinacion_completa(n:int, r:int):
    if r<n: return -1       # solo datos validos
    return r_factorial(n)//(r_factorial(n-r)*r_factorial(r))
