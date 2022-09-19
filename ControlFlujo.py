# Booleans: Son variables True o False, deben empezar con mayúscula
# verdadero = True
# falso = False


# Comparación de  variables
# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b
# # Instrucción "if"
#
# if 2<5:
#     print("2 es menor que 5")

# if 2 == 2 :
#     print("2 es igual a 2")
# if 2 == 3 :
#     print("2 es igual a 3")
# if 2 > 5:
#     print("2 es mayor que 5")
# if 5 < 2 :
#     print("5 es mayor que 2")
# if 2 != 2 :
#     print("2 no es igual a 2")
# if 3 != 2:
#     print("3 no es igual a 2")
# if 3 >= 2 :
#     print("3 es mayor o igual que 2")
# if 3 <= 2 :
#     print("3 es menor o igual que 2")

# Condicionales consecutivas
if 2 > 5 :
    print("lala")
elif 2 > 5:
    print("2 es menor que 5")
else:
    print("yo me imprimo si todo lo demas es false")

# Operadores ternarios: Aplican una estructura diferente para establecer condiciones, se escribe en una sola linea
# "Resultado verdadero" -> "Condicional if" -> "Condicional else" -> "Resultado False"
print("Cuando devuelve True") if 5 > 2 else print("Cuando devuelve False")

# Conector lógico AND: Ambas condiciones deben ser verdaderas para que el resultado sea verdadero y se imprima la String
if 2 < 5 and 3 > 2:
    print("Ambas devuelven True")

# Conector lógico OR: A diferencia de AND, basta que una condición sea verdadera
if 2 > 5 or 3 > 2:
    print("Una de las dos condiciones es verdadera")
