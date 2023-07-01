lenguajes = ["PHP", "Python", "Ruby", "Java"]
"""
lenguajes[1] = "Go"
print(lenguajes[-1])
print(lenguajes[1:3])
print(lenguajes[1:])
print(lenguajes[:3])
"""
lenguajes.insert(3, "Go") # Cambia en el indice que quieres
lenguajes.insert(0, "C")
lenguajes.remove("Java") # Elimina el lenguaje
print(lenguajes)
print("PHP" in lenguajes)
print(len(lenguajes)) # Elementos que tenemos
# lenguajes.clear() eliminar listado