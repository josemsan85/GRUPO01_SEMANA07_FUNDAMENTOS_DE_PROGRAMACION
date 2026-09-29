def eliminar_ocurrencia_n(lista, valor, n):
    # n es la ocurrencia que quieres eliminar (1ª, 2ª, 3ª, etc.)
    contador = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            contador += 1
            if contador == n:
                del lista[i]  # O también: lista.pop(i)
                return True # Confirmamos que se eliminó
    return False # No se encontró esa ocurrencia N
frutas = ["manzana", "pera", "manzana", "uva", "manzana", "banana"]
# Queremos eliminar la 3ª ocurrencia de "manzana"
print(frutas)
eliminar_ocurrencia_n(frutas, "manzana", 3)
print(frutas)
# Resultado: ['manzana', 'pera', 'manzana', 'uva', 'banana']