# Lista

lista = [1, 2, 3]
lista.append(4)

# lista.clear() limpia la lista
lista2 = lista.copy()  # copia una lista
print(lista, lista2)

# lista.count() cuenta cuantas veces se repite un elemento de la lista
print(lista.count(2))

# len(lista) cuenta la longitud de la lista
print(len(lista))

# Indizado de listas
print(lista[2])

# Eliminar ultimo elemento de la lista
# lista.pop()
# print(lista)

# Eliminar un elemento en particular por su valor
# lista.remove(3)
# print(lista)

# Revertir el orden de la lista
# lista.reverse()
# print(lista)

# Ordena la lista siempre y cuando contenga los mismos tipos de datos
# lista.sort()

# Tuplas: son listas inmutables
tupla = ('hola', 'mundo', 'chanchito', 'feliz')
print(tupla)
print(tupla[0])

# Convertir tupla a lista
listaDeTupla = list(tupla)
listaDeTupla.append('perro')
print(listaDeTupla)

#Rangos
rango = range(6)
print(rango)

