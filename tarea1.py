lista = [12, 11, 5, 18, 9, 13]

#bubbleSort
def bubbleSort (lista):
 n = len (lista)

 for i in range (n-1):
        for j in range (n -i-1):

            if lista [j] > lista [j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

 return lista

print (bubbleSort(lista))

#selection sort

def selectionSort (lista):
    n = len (lista)
    for i in range (n-1):
        indexMinimo = 1
        for j in range (i+1,n):
            if lista[j] < lista[indexMinimo]:
                indexMinimo = j
        valorMinimo = lista.pop (indexMinimo)
        lista.insert (i, valorMinimo)

        return lista


print (selectionSort(lista) )

