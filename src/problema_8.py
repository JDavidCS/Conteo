"""
Problema N8
Contruya un programa que cuente los caminos mínimos en la grilla rectangular desde (0,0)
hasta (a,b) moviendose solamente hacia la derecha y hacia arriba
        / a + b \  = / a + b \ 
        \   a   /    \   b   /
 - ingresar a y b
 - calcular el número de caminos mínimos
 - agregar puntos obligatorios por los que el camino debe pasar
 - agregar puntos bloqueados para casos pequeños
 Extensión opcional: dibujar la grilla y algunos caminos usando Python     
"""
from src.combinacion import combinacion

def count_general(a:int, b:int):
    """
    a -> int: Pasos derecha\n
    b -> int: Pasos arriba\n
    """
    return  combinacion(a+b,b)

def count_obligatorio(a:int, b:int, punto: tuple[int,int]):
    """
    a -> int: Pasos derecha\n
    b -> int: Pasos arriba\n
    punto -> (int, int) punto por el que se tiene que pasar\n
    """
    casosAnteriores = count_general(punto[0], punto[1])
    casosSiguientes = count_general(a-punto[0], b-punto[1])
    return casosAnteriores*casosSiguientes
def count_evitar(a:int, b:int, punto: tuple[int,int]):
    """
    a -> int: Pasos derecha\n
    b -> int: Pasos arriba\n
    punto -> (int, int) punto por el que NO se tiene que pasar\n
    """
    casosTotales = count_general(a,b)
    casosEspecificos = count_obligatorio(a,b,punto)
    return (casosTotales-casosEspecificos)
