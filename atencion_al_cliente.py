# EJERCICIO 3: SISTEMA DE ATENCIÓN AL CLIENTE (Cola)

from collections import deque

# Crear la cola
cola = deque()

# a) Implementar tomar_turno(cliente) -> cliente entra a la cola
def tomar_turno(cliente):
    cola.append(cliente)             # enqueue

# b) Implementar atender() -> el primer cliente de la cola es atendido (sale)
def atender():
    if len(cola) > 0:
        atendido = cola.popleft()    # dequeue
        print("Atendido:", atendido)

# c) Implementar mostrar_cola() -> mostrar cuántos esperan y sus nombres
def mostrar_cola():
    print("Cantidad esperando:", len(cola))
    print("Clientes en espera:", list(cola))

# --- d) SIMULACIÓN ---

# 1. Entran 4 clientes
print("--- Entran 4 clientes ---")
tomar_turno("Cliente 1")
tomar_turno("Cliente 2")
tomar_turno("Cliente 3")
tomar_turno("Cliente 4")
mostrar_cola()

# 2. Se atienden 2
print("\n--- Se atienden 2 clientes ---")
atender()
atender()
mostrar_cola()

# 3. Entra 1 cliente más
print("\n--- Entra 1 cliente mas ---")
tomar_turno("Cliente 5")
mostrar_cola()

# 4. Se atienden todos los restantes
print("\n--- Se atienden a todos ---")
while len(cola) > 0:
    atender()

mostrar_cola()