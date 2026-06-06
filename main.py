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
from src.problema_8 import *
from utils.factorial import *
from src.permutacion import *
from src.combinacion import *

def ejemplo_permutacion():
    exec(2,2,1,10)

def ejemplo_caminos():
    var1 = count_general(8,4)                   # Caminos en general
    goto = count_evitar(8,4,(4,2))              # Caminos que pasan por el medio
    limit = count_obligatorio(8,4,(0,4))        # Camino solo por arriba
    limit2 = count_obligatorio(8,4,(8,0))       # Camino solo por derecha
    print("Tenemos un tablero de 8x4")
    print(f"La cantidad de caminos posibles en total es: {var1}")
    print(f"Los caminos que no pasan por (4,2) son: {goto}")
    print(f"Si se asciende totalmente, solo queda {limit} camino (ir a la derecha)")
    print(f"Si se va totalmente a la derecha, solo queda {limit2} camino (ir arriba)")
    
def get_num():
    # recibir números positivos
    numero = 0
    
    while numero <= 0:
        numero = float(input(">> "))
        
        if numero <= 0:
            print("Error: El número no es positivo. Intenta de nuevo.")
            
    return numero
    
def menu():
    print("\n" + "="*20)
    print("        MENÚ PRINCIPAL")
    print("="*30)
    print("1. Insertar información manual")
    print("2. Mostrar una prueba")
    print("3. Salir")
    print("-"*20)
    opcion1 = get_num()
    print("\n" + "="*20)
    print("    SELECCIONA UNA PRUEBA")
    print("="*30)
    print("1. Algoritmo de permutación")
    print("2. Algoritmo de rutas mínimas")
    print("-"*0)
    opcion2 = get_num()
    if opcion1 == 1:
        print("Comming soon...")
    elif opcion1 == 2:
        if opcion2 == 1: ejemplo_permutacion()
        elif opcion2 == 2: ejemplo_caminos()
    
    


menu()

