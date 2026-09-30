# EJERCICIO 1: ORDENAR NOTAS ESTUDIANTILES

def bubble_sort(lista):
    """Ordena una lista en su lugar usando Bubble Sort."""
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break

def selection_sort(lista):
    """Ordena una lista en su lugar usando Selection Sort."""
    n = len(lista)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]


# --- RESOLUCIÓN DEL EJERCICIO ---

# a) Ordenar con Bubble Sort
notas_burbuja = [85, 42, 93, 67, 28, 75]
bubble_sort(notas_burbuja)
print("a) Bubble Sort:")
print(notas_burbuja)

# b) Ordenar con Selection Sort
notas_seleccion = [85, 42, 93, 67, 28, 75]
selection_sort(notas_seleccion)
print("b) Selection Sort:")
print(notas_seleccion)

# c) Mostrar mínima, máxima y promedio
nota_minima = notas_burbuja[0]
nota_maxima = notas_burbuja[-1]
promedio = sum(notas_burbuja) / len(notas_burbuja)

print("c) Estadisticas:")
print("Nota minima:", nota_minima)
print("Nota maxima:", nota_maxima)
print("Promedio:", promedio)