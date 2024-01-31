import random
def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            
            #valor = random.randint(1, 10)
            valor = float(input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): "))
            fila.append(valor)
        matriz.append(fila)
        
    Matrices.append(matriz)
        
    return matriz
#Solicitamos el número de capas
capas = int(input("Digite el numero de capas: "))
#Solicitamos la función de activacion

funcion = input("Digite la función de activacion: ")
#funcion = "2(x)"

# Ejemplo: Separar una cadena en dos partes usando un carácter específico

caracter_separador = "("

# Buscar el índice del carácter separador
indice_separacion = funcion.index(caracter_separador)

# Separar la cadena en dos partes
parte1 = funcion[:indice_separacion]


#Definimos el tamaño del vector y sus valores 

Matrices = []

for i in range(capas + 1):
    print("Matriz: ", (i+1))
    # Pedir al usuario el número de filas y columnas de la matriz
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    #filas = 5
    #columnas = 5

    # Pedir la matriz al usuario
    matriz_ingresada = pedir_matriz(filas, columnas)

    # Mostrar la matriz ingresada

#Hacemos las operacioens

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
                resultado_aux[i][j] += (matriz1[i][k] * matriz2[k][j]) / float(parte1)
    
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
        resultado_final = [[float(parte1) * elemento for elemento in fila]
                           for fila in resultado_final]

        # Realizar la multiplicación con la siguiente matriz
        resultado_final = multiplicar_matrices(resultado_final, matriz)
        print("Resultado despues de la funcion de integración :")
        for fila in resultado_final:
            print(fila)
    return resultado_final

# Multiplicar todas las matrices en la lista en cadena y multiplicar por 2 en cada iteración
try:
    resultado_final = multiplicar_matrices_en_cadena(Matrices)

    print("Resultado Final:")
    for fila in resultado_final:
        print(fila)
except ValueError as e:
    print(f"Error: {e}")