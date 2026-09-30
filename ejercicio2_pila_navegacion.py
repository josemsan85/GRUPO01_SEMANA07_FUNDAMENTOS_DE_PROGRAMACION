#Historial de navegación con una Pila
# - append() para "apilar" (push)
# - pop()    para "desapilar" (pop)
historial = []


def visitar(url):
    """Agrega la página a la pila y muestra la pila actual."""
    historial.append(url)  # push
    print(f"Visitando: {url}")
    print(f"Pila actual: {historial}")


def retroceder():
    """Quita la última página y muestra a dónde regresó."""
    if len(historial) <= 1:
        print("No hay a dónde retroceder.")
        return
    historial.pop()  # pop: saca la página actual
    print(f"Retrocediendo... Ahora estás en: {historial[-1]}")


def pagina_actual():
    """Muestra la página actual sin quitarla de la pila."""
    if not historial:
        print("No hay páginas en el historial.")
        return
    print(f"Página actual: {historial[-1]}")


# Google -> YouTube -> GitHub -> retroceder -> retroceder
visitar("Google")
visitar("YouTube")
visitar("GitHub")
retroceder()
retroceder()
pagina_actual()
