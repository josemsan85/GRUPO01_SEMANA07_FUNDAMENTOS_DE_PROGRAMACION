
cli1 = input("cliente 1 ")
cli2 = input("cliente 2 ")
cli3 = input("cliente 3 ")
cli4 = input("cliente 4 ")

cola = []

#a) Implementar tomar_turno(cliente) → cliente entra a la cola.

def tomarturno (cliente):
    cola.append(cliente)


#b) Implementar atender() → el primer cliente de la cola es atendido (sale).
def atender ():
    cola.pop(0)


#c) Implementar mostrar_cola() → mostrar cuántos esperan y sus nombres.

def mostrarCola (cliente):
    print ( "cantidad de clientes " +  str(len(cliente)) )

    for i in range (0, len(cliente)):
        print(str(cliente[i]))

#d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos

tomarturno(cli1)
tomarturno(cli2)
tomarturno(cli3)
tomarturno(cli4)

atender()
atender()

cli5 = input("cliente 5 ")
tomarturno(cli5)

mostrarCola(cola)
