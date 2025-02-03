###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###
import os
os.system('clear')

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print('Kleyner \nCiudad Guayana')
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print('a:', a, type(a))
print('b:', b, type(b))
print('c:', c, type(c))
print('d:', d, type(d))
print('e:', e, type(e))
print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
transform_to_integer = int("12345")
print(float(transform_to_integer))

print(int(3.99))
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
my_name = 'Kleyner'
my_age = 38
my_heigth = 1.86

print(f'\n Mi nombre es: {my_name}, mi edad es: {my_age} y mido: {my_heigth}\n')

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


var_pi = round(3.14/2)
print(f'el valor es {var_pi}')