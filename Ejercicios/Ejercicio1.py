# Sentencia input: solicita datos ingresados por el tecldado
dato = input("Ingrese dato")

# Sentencia: es una expresión ejecutable nativa del lenguaje de programación
# Método: es proceso ejecutable perteneciente a un tipo de dato

# Este ejercicio consiste en la utilización de la sentencia input para toma de datos ingresados por el usuario,
# se crea una lista de datos y por ultimo mediante las sentencias if y else creamos un proceso condicional en el cual se
# comprueba la existencia de los datos ingresados en input con la utilización de el método count, el cual sirve para
# contar cuantas veces se repite un elemento en una lista de datos

lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']
if lista.count(dato) > 0:
    print("El dato existe")
else:
    print("El dato no existe")

