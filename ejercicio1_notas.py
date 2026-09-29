#Ordenar notas

def bubble_sort(lista):
    """Utilice Bubble Sort para ordenar la lista."""
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista


def selection_sort(lista):
    """Selection Sort para ordenar la lista."""
    n = len(lista)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]
    return lista



notas= [85, 42, 93, 67, 28, 75]

# a) Bubble Sort
notas_bubble = bubble_sort(notas.copy())
print("a) Ordenado con Bubble Sort:   ", notas_bubble)

# b) Selection Sort
notas_selection = selection_sort(notas.copy())
print("b) Ordenado con Selection Sort:", notas_selection)

# c) Mínimo, máximo y promedio
nota_min = min(notas)
nota_max = max(notas)
promedio = sum(notas) / len(notas)

print(f"c) Nota mínima:  {nota_min}")
print(f"   Nota máxima:  {nota_max}")
print(f"   Promedio:     {promedio:.2f}")
