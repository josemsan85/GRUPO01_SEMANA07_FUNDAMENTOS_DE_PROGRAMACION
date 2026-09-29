notas = [85, 42, 93, 67, 28, 75]
print(f"Lista de notas: {notas}")
def bubble_sort(lista):
    n = len(lista)
    for i in range (n):
        intercambiado = False
        for j in range (0, n-i-1):
            if lista[j] > lista [j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
bubble_sort(notas)
print(f"Lista de notas ordenada mediante Bubble Sort: {notas}")
def selection_sort(lista):
    n = len(lista)
    for i in range (n-1):
        idx_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
            if idx_min != i:
                lista[i], lista[idx_min] = lista[idx_min], lista[i]
selection_sort(notas)
print(f"Lista de notas ordenadas mediante Selection Sort: {notas}")
maxima = notas[0]
minima = notas[0]
suma_notas = 0
for i in range(len(notas)):
    if notas [i] > maxima:
        maxima = notas [i]
    if notas [i] < minima:
        minima = notas [i]
    suma_notas += notas[i]
    promedio = suma_notas / len(notas)
print(f"Nota maxima: {maxima}")
print(f"Nota minima: {minima}")
print(f"Promedio: {promedio:.2f}")