"""
Problema N1
Programa con permutaciones y k-permutaciones:
 - calcular n!
 - calcular P(n,r)
 - validar que n y r sean enteros no negativos
 - mostrar el procedimiento usado
 - comparar al menos dos casos, P(10,3) y P(20,5)
 - comparar una versión recursiva y una iterativa

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
from src.problema_1 import exec
from utils.factorial import *
from src.permutacion import *
from src.combinacion import *

# exec()
# print(div_factorial(8,6))
# print(combinacion(8,2))

