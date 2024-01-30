Matrices = []

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

# Pedir al usuario el número de filas y columnas de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Pedir la matriz al usuario
matriz_ingresada = pedir_matriz(filas, columnas)

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Pedir la matriz al usuario
matriz_ingresada = pedir_matriz(filas, columnas)
# Mostrar la matriz ingresada
print("Matriz ingresada:")
for fila in Matrices:
    print(fila)