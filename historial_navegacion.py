# EJERCICIO 2: SISTEMA DE HISTORIAL DE NAVEGACIÓN (Pila)

historial = []

# a) Agregar página a la pila y mostrar la pila actual
def visitar(url):
    historial.append(url)
    print("Visito:", url)
    print("Historial actual:", historial)

# b) Quitar la última página y mostrar a dónde regresó
def retroceder():
    if len(historial) > 0:
        historial.pop()
        if len(historial) > 0:
            print("Regreso a:", historial[-1])
        else:
            print("Historial vacio, no hay paginas anteriores")

# c) Mostrar la página actual sin quitarla
def pagina_actual():
    if len(historial) > 0:
        print("Pagina actual:", historial[-1])

# --- d) PRUEBAS SOLICITADAS ---

visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()