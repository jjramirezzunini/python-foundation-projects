diccionario = {
    "nombre": "Chanchito",
    "raza": "Persa",
    "edad": 5
}
# print(diccionario)
# print(diccionario["nombre"])
# print(diccionario["raza"])
# print(diccionario.get("nombre"))
# diccionario["nombre"] = "Fluffy"
# print(diccionario["nombre"])

# print(len(diccionario))

# Agregar valores al diccionario
diccionario["ronronea"] = "si"
print(diccionario)

# Eliminar el valor seleecionado
# diccionario.pop("ronronea")
# print(diccionario)

# Eliminar el ultimo valor del diccionario
# diccionario.popitem()

# copiar un diccionario
# copiaGatito = diccionario.copy()
# copiaGatito = dict(diccionario)

# Eliminar valor seleccionado
# del diccionario["ronronea"]
# print(diccionario, copiaGatito)

# Diccionarios anidados
gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}

# Utilización del constructor dict
perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)