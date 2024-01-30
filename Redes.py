
def pedir_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): "))
            fila.append(valor)
        matriz.append(fila)
        Matrices.append(matriz)
        
    return matriz
#Solicitamos el número de capas
capas = int(input("Digite el numero de capas: "))
#Solicitamos la función de activacion
funcion = input("Digite la función de activacion: ")


# Ejemplo: Separar una cadena en dos partes usando un carácter específico

caracter_separador = "("

# Buscar el índice del carácter separador
indice_separacion = funcion.index(caracter_separador)

# Separar la cadena en dos partes
parte1 = funcion[:indice_separacion]


#Definimos el tamaño del vector y sus valores 

Matrices = []

for i in range(capas):
    # Pedir al usuario el número de filas y columnas de la matriz
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Pedir la matriz al usuario
    matriz_ingresada = pedir_matriz(filas, columnas)

    # Mostrar la matriz ingresada
    print("Matriz ingresada:")
    for fila in Matrices:
        print(fila)