###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

# Podemos importar módulos de Python para usarlos en nuestros programas.
# En este caso, importamos el módulo "os" que nos da acceso a funciones
# relacionadas con el sistema operativo
import os
# system() nos permite ejecutar un comando en la terminal
# en este caso lo hacemos para limpiar la pantalla
os.system("clear")

print("\n Sentencia simple condicional")

# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript: 
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# En un pueblo de Isla Margarita son más laxos y
# te dejan conducir si eres mayor de edad O tienes carnet
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil sería:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print('----Determinemos el numero mayor-----\n')

number_one = int(input('Introduce el primer numero por favor:\n'))
number_two = int(input('Introduce el segundo numero por favor:\n'))
if number_one == number_two:
  print(f'{number_one} y {number_two} son iguales')
elif number_one > number_two:
  print(f'{number_one} es mayor que {number_two}')
else : 
  print(f'{number_two} es mayor que {number_one}')

print('\n-------------------------------------\n')
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print('\ncalculadora de operaciones simples\n')
z = input('por favor introduce un operador entre los sieguientes ( "+" , "-" , "*" , "/" )\n')
x = int(input('Introduce el primer numero por favor:\n'))
y = int(input('Introduce el segundo numero por favor:\n'))


if (y != 0) and (z == '/'):
  print(f'la division de {x} / {y} es = {x/y}')
elif z == '*':
  print(f'la multiplicacion de {x} * {y} es = {x*y}')
elif z == '+':
  print(f'la suma de {x} + {y} es = {x+y}')
elif z == '-':
  print(f'la resta de {x} - {y} es = {x-y}')
else: print('valores incorrectos la operacion no puede ser ejecutada')

print('\n-------------------------------------\n')
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print('\n------Determina si el año es bisiesto------\n')
evaluated_year = int(input('introduzca un año por favor:'))

if (evaluated_year % 400 == 0) or ((evaluated_year % 4 == 0) and (evaluated_year % 100 != 0)):
  print ('es un año bisiesto')   
else: print ('no es un año bisiesto')

print('\n-------------------------------------\n')
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print('\n------Clasificacion de edades------\n')
age = int(input('introduce una edad por favor:'))
if (age >= 65):
  print ('Clasificado como : Adulto mayor')
elif age >= 18 :
  print ('Clasificado como : Adulto')
elif age >= 13 :
  print ('Clasificado como : Adolescente')
elif age >= 3: 
  print ('Clasificado como : Niño')
else: print ('Clasificado como : Bebe')
  
