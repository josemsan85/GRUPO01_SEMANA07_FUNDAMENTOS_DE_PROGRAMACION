#google youtube

pagina  = input("coloca la primera pagina ")
pagina2 = input ("coloca la segunda pagina ")


stack = []

stack.append(pagina)
stack.append(pagina2)


#a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
print(stack)
#b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
stack.pop()
print (stack[-1])
#c) Implementar pagina_actual() → muestra la página actual sin quitarla

pagina3 = input ("coloca la tercera pagina ")
stack.append(pagina3)
print (stack[-1])

#d) Probar con: Google → YouTube → GitHub → retroceder → retroceder

