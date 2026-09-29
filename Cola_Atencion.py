from collections import deque
cola = deque()
def tomar_turno(cliente):
    cola.append(cliente)
    print(f"Llegó {cliente} y tomó un turno.")
def atender():
    if cola:
        cliente_atendido = cola.popleft()
        print(f"Atendiendo a: {cliente_atendido}")
    else:
        print("No hay clientes en espera.")
def mostrar_cola():
    print(f"\n--- ESTADO DE LA COLA ---")
    print(f"Clientes en espera: {len(cola)}")
    print(f"Lista de espera: {list(cola)}")
    print("-------------------------\n")
print("=== INICIO DE LA SIMULACIÓN ===\n")
tomar_turno("Carlos")
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("María")
mostrar_cola()
atender()
atender()
mostrar_cola()
tomar_turno("Jorge")
mostrar_cola()
print("--- Atendiendo a todos los clientes restantes ---")
while cola:
    atender()
mostrar_cola()