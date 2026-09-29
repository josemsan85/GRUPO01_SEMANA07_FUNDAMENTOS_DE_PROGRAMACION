historial = []
def visitar(url):
    historial.append(url)
    print(f"Visitando {url} -> Pila actual: {historial}")
def retroceder():
    if len(historial) > 1:
        historial.pop()
        print(f"Retrocediendo... Ahora estás en: {pagina_actual()}")
    elif len(historial) == 1:
        historial.pop()
        print("Retrocediendo... El historial ahora está vacío.")
    else:
        print("No hay páginas en el historial para retroceder.")
def pagina_actual():
    if historial:
        return historial[-1]
    return "Ninguna (Historial vacío)"
print("--- PRUEBA DEL SISTEMA DE NAVEGACIÓN ---")
visitar("Google")
visitar("YouTube")
visitar("GitHub")
print(f"\nPágina actual: {pagina_actual()}\n")
retroceder()
retroceder()
print(f"\nPágina actual final: {pagina_actual()}")