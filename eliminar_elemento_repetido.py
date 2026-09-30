# EXTRA 2: ELIMINAR EL SEGUNDO ELEMENTO REPETIDO

fruta = ['uva', 'pera', 'uva', 'naranja']
print("Lista inicial:", fruta)

# Forma algorítmica buscando con índices y contador:
contador = 0
for i in range(len(fruta)):
    if fruta[i] == 'uva':
        contador += 1
        if contador == 2:             # Cuando encontramos el segundo 'uva'
            fruta.pop(i)              # Eliminamos por su índice 'i'
            break                     # Salimos del ciclo

print("Lista final:", fruta)