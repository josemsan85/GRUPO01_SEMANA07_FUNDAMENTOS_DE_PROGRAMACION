#Lista de frutas
frutas = ["Naranja", "Fresa", "Pera", "Uva", "Piña", "Fresa", "Sandia", "Fresa"]
print("Lista original:", frutas)

contador = 0

for i in range(len(frutas)):
    if frutas[i] == "Fresa":
        contador += 1              # cuento cada Fresa que encuentro
        if contador == 2:          # cuando es la segunda
            frutas.pop(i)          # la elimino por su posición
            break                  # y dejo de recorrer

print("Lista final:", frutas)

#Resultado
"""
Lista original: ['Naranja', 'Fresa', 'Pera', 'Uva', 'Piña', 'Fresa', 'Sandia', 'Fresa']
Lista final: ['Naranja', 'Fresa', 'Pera', 'Uva', 'Piña', 'Sandia', 'Fresa']
"""
