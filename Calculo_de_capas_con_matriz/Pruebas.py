def multiplicar_matrices(matriz1, matriz2):
   
    filas1, columnas1 = len(matriz1), len(matriz1[0])
    filas2, columnas2 = len(matriz2), len(matriz2[0])

    # Verificar si las matrices pueden multiplicarse
    if columnas1 != filas2:
        raise ValueError("Las matrices no pueden multiplicarse debido a dimensiones incorrectas.")

    # Inicializar la matriz de resultado con ceros
    resultado = [[0 for _ in range(columnas2)] for _ in range(filas1)]
    resultado_aux = [[0 for _ in range(columnas2)] for _ in range(filas1)]
    
    # Realizar la multiplicación
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(filas2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
                resultado_aux[i][j] += (matriz1[i][k] * matriz2[k][j])/2
    
    print("Resultado antes de la función:")
    for fila in resultado_aux:
        print(fila)
        
    return resultado


def multiplicar_matrices_en_cadena(lista_de_matrices):
    if len(lista_de_matrices) < 2:
        raise ValueError(
            "Se requieren al menos dos matrices para la multiplicación.")

    resultado_final = lista_de_matrices[0]

    for matriz in lista_de_matrices[1:]:
        # Multiplicar por 2 cada elemento de la matriz resultante
        resultado_final = [[2 * elemento for elemento in fila]
                           for fila in resultado_final]

        # Realizar la multiplicación con la siguiente matriz
        resultado_final = multiplicar_matrices(resultado_final, matriz)
        print("Resultado despues de la funcion de integración :")
        for fila in resultado_final:
            print(fila)
    return resultado_final

# Ejemplo de uso
matrices_en_lista = [
    [[-3, 1, 4, -2]],

    [[44, 64],
     [44, 64],
     [52, 80],
     [56, 84]]

]


# Multiplicar todas las matrices en la lista en cadena y multiplicar por 2 en cada iteración
try:
    resultado_final = multiplicar_matrices_en_cadena(matrices_en_lista)

    print("Resultado Final:")
    for fila in resultado_final:
        print(fila)
except ValueError as e:
    print(f"Error: {e}")
