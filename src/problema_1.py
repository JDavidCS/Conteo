"""
Problema N1
Programa con permutaciones y k-permutaciones:
 - calcular n!
 - calcular P(n,r)
 - validar que n y r sean enteros no negativos
 - mostrar el procedimiento usado
 - comparar al menos dos casos, P(10,3) y P(20,5)
 - comparar una versión recursiva y una iterativa
"""
"""
Implementación:
    Para comparar la forma recursiva del programa y la forma iterativa
    se observa que no en todas las ejecuciones la diferencia de tiempo 
    es la misma, por lo que se optó por repeter 10 veces la ejecución 
    y sacar un promedio. Adicional, poder cambiar los parámetros de la
    función: n aumenta en m, k veces. Es decir, se calcula k tiempos
    distintos comenzando desde n hasta n+(m*k)
    A lo ultimo se hace la diferencia Iterativo - Recursivo. Para mostrar
    cual tuvo mejor rendimiento.
"""
from src.permutacion import *
import time

def exec(n:int, r:int, m:int, k:int):
    """
    Ejecuta y muestre resultados comparativos entre\n
    programación recursiva e iterativa\n
    n -> int: cantidad elementos\n
    r -> int: tamaño del grupo\n
    m -> int: incremento de los elementos\n
    k -> int: cantidad de pruebas
    return -1 en caso de error
    """
    if r<n: return -1
    prom = 0
    datos = []
    datosR = []
    # promedio permutación normal
    for i in range(k):
        sum=0
        for j in range(10):
            start = time.perf_counter()
            permutacion(n+(m*i),r)
            end = time.perf_counter()
            sum += (end-start)
        prom=sum/10
        datos.append(prom)
    # promedio permutacion recursiva
    for i in range(k):
        sum=0
        for j in range(10):
            start = time.perf_counter()
            r_permutacion(n+(m*i),r)
            end = time.perf_counter()
            sum += (end-start)
        prom=sum/10
        datosR.append(prom)

    print("------------RESULTADOS INDIVIDUALES------------")
    print(f"{k} números de prueba, r = {r} (constante)")
    print("valor n\t  Diferencia de ejecusión\t Funcion más rapida\n")

    for i in range(k):
        dif = abs(datos[i] - datosR[i])
        msg = "Función recursiva" if (datos[i] - datosR[i])<0 else "Función iterativa"
        print(f"n = {int(n+(m*i))} \t {dif: .12f} \t\t", msg)
    print("-----------------------------------------------")

