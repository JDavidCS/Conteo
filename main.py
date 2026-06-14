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
    exec(2,2,1,10)        # n: cantidad de elementos, r: tamaño del grupo; m: incremento de los elementos; r: cantidad de pruebas

def ejemplo_caminos():
    var1 = count_general(8,4)                   # a: pasos a la derecha; b: pasos a la izquierda
    goto = count_evitar(8,4,(4,2))              # a,b; Tupla: punto a evitar (derecha,izquierda)
    limit = count_obligatorio(8,4,(0,4))        # a,b; Tupla: punto obligatorio (derecha,izquierda)
    limit2 = count_obligatorio(8,4,(8,0))       # a,b; Tupla: punto obligatorio (derecha,izquierda)
    print("Tenemos un tablero de 8x4")
    print(f"La cantidad de caminos posibles en total es: {var1}")
    print(f"Los caminos que no pasan por (4,2) son: {goto}")
    print(f"Si se asciende totalmente, solo queda {limit} camino (ir a la derecha)")
    print(f"Si se va totalmente a la derecha, solo queda {limit2} camino (ir arriba)")
    
def get_option(*args):
    option = 0
    while True:
        option = int(input(">> "))
        
        if option not in args:
            print("Error: Opción no disponible. Intenta de nuevo.")
            continue
        break
    return option
    
def get_num(msg):
    # recibir números positivos
    numero = 0
    
    while True:
        numero = int(input(msg+"  >> "))
        
        if numero < 0:
            print("Error: El número no mayor a 0. Intenta de nuevo.")
            continue
        break    
    return numero
    
def permutacion():
    print("\n" + "="*30)
    print("Se va a Mostrar una serie de pruebas comparando\nla permutación con ciclos iterativos y recursión")
    print("n y r son los dos datos para la permutación.")
    print("NECESARIAMENTE n>=r")
    print("luego se van a hacer varias pruebas cambiando el valor de n")
    print("m es el intervalo con el que va a crecer n en cada prueba")
    print("k es el número de pruebas")
    while True:
        n = get_num("\ninserte n")
        r = get_num("inserte r")
        if n<r:
            print("*-"*4+" ¡n DEBE SER MAYOR O IGUAL A r! ","*-"*4)
            continue
        break
    m = get_num("inserte m")
    k = get_num("inserte k")
    exec(n,r,m,k)
    
def caminos():
    print("="*30)
    print("1. Caminos posibles en total")
    print("2. Caminos posibles sin un punto")
    print("3. Caminos pasando por un punto")
    print("="*30)
    option = get_option(1,2,3)
    if option == 1:
        print("\nInserta los datos:")
        a = get_num("a")
        b = get_num("b")
        res = count_general(a,b)
        print(f"La cantidad de caminos posibles es: {res}")
    elif option == 2:
        print("\nInserta los datos:")
        a = get_num("a")
        b = get_num("b")
        print("Punto (a,b)")
        pa = get_num("(a, )")
        pb = get_num("( ,b)")
        res = count_evitar(a,b, (pa, pb))
        print(f"Caminos sin ({pa},{pb}): {res}")
    else:
        print("\nInserta los datos:")
        a = get_num("a")
        b = get_num("b")
        print("Punto (a,b)")
        pa = get_num("(a, )")
        pb = get_num("( ,b)")
        res = count_obligatorio(a,b, (pa, pb))
        print(f"Camino que pasan por ({pa},{pb}): {res}")

def menu():
    print("\n" + "="*30)
    print("        MENÚ PRINCIPAL")
    print("="*30)
    print("1. Insertar información manual")
    print("2. Mostrar una prueba")
    print("3. Salir")
    print("-"*20)
    opcion1 = get_option(1,2,3)
    print("\n" + "="*30)
    print("    SELECCIONA UNA PRUEBA")
    print("="*30)
    print("1. Algoritmo pruebas de permutación")
    print("2. Algoritmo de rutas mínimas")
    print("-"*0)
    opcion2 = get_option(1,2)
    if opcion1 == 1:
        if opcion2 == 1: permutacion()
        elif opcion2 == 2: caminos()
    elif opcion1 == 2:
        if opcion2 == 1: ejemplo_permutacion()
        elif opcion2 == 2: ejemplo_caminos()
        
menu()

