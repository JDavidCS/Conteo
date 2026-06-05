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
 - agregar puntos bloqueados para casos bloqueados
 Extensión opcional: dibujar la grilla y algunos caminos usando Python     
"""
from src.permutacion import *
import time

n = 2          # valor inicial n
r = 2
m = 1          # aumento por iteración
k = 10           # cantidad de datos
prom = 0
datos = []
datosR = []
for i in range(k):
    sum=0
    for j in range(10):
        start = time.perf_counter()
        permutacion(n+(m*i),r)
        end = time.perf_counter()
        sum += (end-start)
    prom=sum/10
    datos.append(prom)

for i in range(k):
    sum=0
    for j in range(10):
        start = time.perf_counter()
        r_permutacion(n+(m*i),r)
        end = time.perf_counter()
        sum += (end-start)
    prom=sum/10
    datosR.append(prom)

for i in range(k):
    dif = datos[i] - datosR[i]
    print(f"n = {int(n+(m*i))}: {dif: .12f}")



# start = time.perf_counter()
# permutacion(n,r)
# end = time.perf_counter()
# tiempo_total1 = end-start
# print(f"permutación normal: {tiempo_total1: .10f}")

# start = time.perf_counter()
# r_permutacion(n,r)
# end = time.perf_counter()
# tiempo_total2 = end-start
# print(f"permutación recursiva: {tiempo_total2: .10f}")

# total = tiempo_total1-tiempo_total2
# print(f"F1 - F2:\n {total: .10f}")