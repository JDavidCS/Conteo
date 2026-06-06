from utils.factorial import *

def permutacion(n:int, r:int):
    """
    versión iterativa \n
    n -> Elementos totales \n
    k -> Tamaño del grupo
    """
    if n < 1 or r < 1: return -1    # solo datos validos
    
    return factorial(n)//factorial(n-r)

def r_permutacion(n:int, r:int):
    """
    versión recursiva \n
    n -> Elementos totales \n
    k -> Tamaño del grupo
    """
    if n < 1: return -1            # solo datos validos
    return r_factorial(n)//r_factorial(n-r)
    