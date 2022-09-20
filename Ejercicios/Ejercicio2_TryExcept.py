# Utilizando input crearemos una calculadora

# Python recibe datos ingresados por input en formato String, por tanto tenemos que transformarlos
# a Integer utilizando la sentencia int

# Sin embargo, si ingresamos un dato que contenga letras e intentamos transformarlo en Int, Python retornará
# un error. Por tanto para eso utilizaremos las sentencias try y except para manejar el flujo de errores durante los
# procesos del programa.
#Try: intenta realizar una acción
#Except: En caso de que la acción de try no sea posible, except evita el mensaje de error y retornará una acción distinta

primero = input('Ingrese el primer número:')
try:
    primero = int(primero)
except:
    print("El valor ingresado no es un número entero")
    exit()
# La sentencia exit termina el proceso después de la excepción

segundo = input('Ingrese el segundo número:')
try:
    segundo = int(segundo)
except:
    print("El valor ingresado no es un número entero")
    exit()

# Condicional para reconocer la operacion
simbolo = input("Ingrese la operación: ")
if simbolo == "+":
    print(primero + segundo)
elif simbolo == "-":
    print(primero - segundo)
elif simbolo == "*":
    print(primero * segundo)
elif simbolo == "/":
    print(primero / segundo)
else:
    print("Ingrese un símbolo válido")


