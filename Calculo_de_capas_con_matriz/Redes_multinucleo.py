import random

import time

# Guarda el tiempo de inicio
inicio = time.time()
from concurrent.futures import ThreadPoolExecutor

def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 10)
            fila.append(valor)
        matriz.append(fila)
        
    return matriz

def multiplicar_matrices(matriz1, matriz2):
    filas1, columnas1 = len(matriz1), len(matriz1[0])
    filas2, columnas2 = len(matriz2), len(matriz2[0])

    if columnas1 != filas2:
        raise ValueError("Las matrices no pueden multiplicarse debido a dimensiones incorrectas.")

    resultado = [[0 for _ in range(columnas2)] for _ in range(filas1)]

    for i in range(filas1):
        for j in range(columnas2):
            for k in range(filas2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def multiplicar_matrices_en_cadena(lista_de_matrices):
    if len(lista_de_matrices) < 2:
        raise ValueError("Se requieren al menos dos matrices para la multiplicación.")

    resultado_final = lista_de_matrices[0]

    with ThreadPoolExecutor() as executor:
        futures = []
        for matriz in lista_de_matrices[1:]:
            futures.append(executor.submit(multiplicar_matrices, resultado_final, matriz))
        
        for future in futures:
            resultado_final = future.result()

    return resultado_final

# Solicitar el número de capas
capas = int(input("Digite el numero de capas: "))

# Crear matrices
Matrices = []
for i in range(capas + 1):
    print("Matriz:", (i + 1))
    filas = 98
    columnas = 98
    matriz_ingresada = pedir_matriz(filas, columnas)
    Matrices.append(matriz_ingresada)

try:
    # Multiplicar matrices en cadena y en paralelo
    resultado_final = multiplicar_matrices_en_cadena(Matrices)

    #print("Resultado Final:")
    #for fila in resultado_final:
     #   print(fila)
except ValueError as e:
    print(f"Error: {e}")
fin = time.time()

# Calcula la diferencia para obtener el tiempo total de ejecución
tiempo_total = fin - inicio

print(f"Tiempo de ejecución: {tiempo_total} segundos")