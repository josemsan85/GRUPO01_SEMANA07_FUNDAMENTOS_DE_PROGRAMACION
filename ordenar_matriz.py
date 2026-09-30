# EXTRA 1: ORDENAR MATRIZ 3x3 CON ÍNDICES

# Matriz 3x3 desordenada inicial
matriz = [
    [1, 3, 4],
    [5, 8, 9],
    [2, 6, 7]
]

# Paso 1: Extraer elementos a una lista usando índices
lista_plana = []
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        lista_plana.append(matriz[i][j])

# Paso 2: Ordenar con Bubble Sort (visto en clase)
n = len(lista_plana)
for i in range(n):
    intercambiado = False
    for j in range(0, n - i - 1):
        if lista_plana[j] > lista_plana[j+1]:
            lista_plana[j], lista_plana[j+1] = lista_plana[j+1], lista_plana[j]
            intercambiado = True
    if not intercambiado:
        break

# Paso 3: Reconstruir la matriz 3x3 ordenada usando índices
matriz_ordenada = []
idx = 0
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(lista_plana[idx])
        idx += 1
    matriz_ordenada.append(fila)

print("Matriz 3x3 ordenada:")
print(matriz_ordenada)