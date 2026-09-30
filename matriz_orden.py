matriz = [
    [85, 42, 93],
    [67, 28, 75],
    [11, 64, 25]
]
print(f"{matriz}")
def bubble_sort(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    n = filas * columnas
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            fila_actual = j // columnas
            columna_actual = j % columnas
            fila_siguiente = (j + 1) // columnas
            columna_siguiente = (j + 1) % columnas
            if matriz[fila_actual][columna_actual] > matriz[fila_siguiente][columna_siguiente]:
                matriz[fila_actual][columna_actual], matriz[fila_siguiente][columna_siguiente] = \
                matriz[fila_siguiente][columna_siguiente], matriz[fila_actual][columna_actual]
                intercambiado = True
        if not intercambiado:
            break
bubble_sort(matriz)
print(f"{matriz}")