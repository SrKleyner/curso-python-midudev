#EJERCIOCIOS DE FUNCIONES
import os
os.system('clear')
# def espacited_numbers(multiplo, maximus):
#     sum = 0
#     value = 0
#     for index, valor in enumerate(range(multiplo, maximus + 1, multiplo)):
#         print(f'Para la iteracion {index} el valor es {valor}')
#         sum = index
#         value = valor
#     print(f'del multiplo {multiplo} se encontraron {sum} valores operables siendo el ultimo posible {value}') 
# multiplo = int(input(f'por favor introduzca un numero entero positivo como multiplo a aumentar: '))
# maximo = int(input(f'por favor introduzca el numero final al cual llegar:'))

# espacited_numbers(multiplo, maximo)

# def media(lista):
#     """ calcula la media de la lista ingresada """
#     if (lista):
#         return sum(lista) / len(lista)
#     else: return print('la lista esta vacia')

# lista = [1, 2, 4, 5, 7, 9]
# print(media(lista))

def make_list_of_integers():
    new_list = []
    i = True
    option = 'y'
    while i:
        if option == 'y':
            os.system('clear')
            new_item = input('introduzca el elemento a cargar en la lista: ')
            try:
                new_list.append(int(new_item))
            except:
                print('el elemento que intento ingresar no es un numero por\n lo que se detendra la ejecucion')
                return new_list[:len(new_list)] if len(new_list) > 0 else [0]
        else:
            i = False
            return new_list
        option = input('Desea continuar cargando elementos a la lista Y/N: ').lower()
        
def make_list():
    new_list = []
    i = True
    option = 'y'
    while i:
        if option == 'y':
            os.system('clear')
            new_item = input('introduzca el elemento a cargar en la lista: ')
            try:
                new_list.append(str(new_item))
            except:
                print('el elemento que intento ingresar no es una cadena por\n lo que se detendra la ejecucion')
                return new_list[:len(new_list)] if len(new_list) > 0 else [0]
        else:
            i = False
            return new_list
        option = input('Desea continuar cargando elementos a la lista Y/N: ').lower()

def maximo(lista):
    num_max = 0
    if not(len(lista)):
        return print(f'la lista {lista} no es valida para la operacion')
    
    for num in lista:
        if num_max < num :
            num_max = num
    print(f'Para la lista {lista} el numero maximo es {num_max}')

lista = make_list()
print(lista)

