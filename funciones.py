"""
def hola(nombre, mas_nombre):#parametros
     print("Hola mundo")
     print(f"Python {nombre} {mas_nombre}")


hola("PHP", "Java") #argumentos
hola("C", "Go")
"""
def hola(nombre, mas_nombre = "Otros"):#parametros
     print("Hola mundo")
     print(f"Python {nombre} {mas_nombre}")


hola("PHP", "Java") #argumentos
hola("C")