###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "midudev"
for caracter in cadena:
  print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
  print(f"El índice es {idx} y la fruta es {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")


# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  print(animal)
  if animal == "loro":
    print(f"El loro está escondido en el índice {idx}")
    break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": continue
  
  print(animal)

# Comprensión de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

###
# EJERCICIOS (for)
###
import os
os.system('clear')
# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:\n")
for index, element in enumerate(range(2,22,2)):
  print (f'el elemento:  {element} se encuentra en el indice: {index}')
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:\n")
size =  len(numeros)
element = 0
for value in numeros:
  element += value

print(f'la media de la lista es : {element/size}')

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:\n")
valor = 0
position = 0
for index, element in enumerate(numeros):
  if element > valor:
    position = index
    valor = element

print(f'el maximo es:{valor} y se encuenra en la posicion:{position} de la lista.')

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "pedro"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:\n")
new_list = []
for element in palabras:
  if len(element) >= 5:
    new_list.append(element)
print(new_list)
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letra = input('introduce una letra:').lower()
palabras.sort(key=str.lower)
sum = 0
for palabra in palabras:
  if letra in palabra[0]:
    sum += 1
    print(f'la palabra numero {sum} que cumple el requisito es {palabra}\n')
if sum > 0:
  print(f'la cantidad de palabras que cumplen el requisito son: {sum}')
else: print('no existen coincidencias para la letra seleccionada en la lista registrada')