#Sistema de atención al cliente con una Cola 

from collections import deque

# deque es una lista optimizada para agregar/quitar por los extremos.
# - append()   para "encolar" (entra al final)
# - popleft()  para "atender" (sale el primero)
cola = deque()


def tomar_turno(cliente):
    """El cliente entra a la cola."""
    cola.append(cliente)  # enqueue
    print(f"{cliente} tomó turno.")


def atender():
    """El primer cliente de la cola es atendido (sale)."""
    if not cola:
        print("No hay clientes esperando.")
        return
    cliente = cola.popleft()  # dequeue
    print(f"Atendiendo a: {cliente}")


def mostrar_cola():
    """Muestra cuántos esperan y sus nombres."""
    print(f"Clientes en espera ({len(cola)}): {list(cola)}")


# ── Simulación pedida en el ejercicio ───────────────────────
# 4 clientes entran, se atienden 2, entra 1 más, se atienden todos.
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carla")
tomar_turno("Pedro")
mostrar_cola()

atender()
atender()
mostrar_cola()

tomar_turno("Sofía")
mostrar_cola()

atender()
atender()
atender()
mostrar_cola()
