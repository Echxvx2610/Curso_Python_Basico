# Listas
Hay cuatro tipos de estructuras de datos en Python :

* Lista [] : es una colección ordenada y modificable. Permite miembros duplicados.
* Tuple() : es una colección ordenada y no modificable (inmutable). Permite miembros duplicados.
* Set{} : es una colección no ordenada, no indexada y no modificable, pero podemos añadir nuevos elementos al conjunto.
No permite miembros duplicados.
* Diccionario{ key:value }: es una colección desordenada, modificable e indexada. No admite miembros duplicados.
Una lista es una colección de diferentes tipos de datos ordenada y modificable. Una lista puede estar vacía o tener elementos de diferentes tipos de datos.

## Crear una lista
En Python podemos crear listas de dos formas:

Usando la función integrada de lista:
```python
# syntax
lst = list()
```
```python
empty_list = list() # esta es una lista vacia,no tiene elementos en ella
print(len(empty_list)) # 0
```
En Python podemos crear listas de dos formas:
Usando corchetes, []
```python
# syntax
lst = []

empty_list = [] # esta es una lista vacia,no tiene elementos en ella
print(len(empty_list)) # 0
```
Listas con valores iniciales. Usamos len() para encontrar la longitud de una lista.
```python
fruits = ['banana', 'orange', 'mango', 'lemon']                     # lista de frutas
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # lista de vegetales
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # lista de productos animales
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # lista de tecnologias web
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # lista de paises

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```
Las listas pueden tener elementos de distintos tipos de datos
```python
 lst = ['Cristian', 21, True, {'country':'Mexico', 'city':'Ensenada'}] # lista con diferentes tipos de datos
```
## Acceso a los Items de una Lista por Index
Accedemos a cada elemento de una lista utilizando su índice. El índice de una lista empieza por 0. La imagen siguiente muestra claramente dónde empieza el índice"
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/79e43902-3f51-45b6-806e-f638591032f1)
```python
fruits = ['manzana', 'platano', 'fresa', 'pera']
first_fruit = fruits[0] # accesamos al primer elemento o item de la lista frutas
print(first_fruit)      # manzana
second_fruit = fruits[1]
print(second_fruit)     # platano
last_fruit = fruits[3]
print(last_fruit) # fresa
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```
## Acceso a los Items de una Lista por Index (negativo)
La indexación negativa significa empezar por el final, -1 se refiere al último elemento, -2 al penúltimo.
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/c0bf0e03-f187-4886-b759-7e9381d2d632)

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

## Desempacando Listas
```python
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```
## Cortando items de Listas
Indexación positiva: Podemos especificar un rango de índices positivos especificando el inicio, fin y paso, el valor de retorno será una nueva lista. (valores por defecto para start = 0, end = len(lst) - 1 (último elemento), step = 1)
```python
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # retorna todos los elementos

all_fruits = fruits[0:] # mismo caso solo no especificamos el tamaño
orange_and_mango = fruits[1:3] # no incluye el index 0 y el 4
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # retorna todos los elementos del ultimo al primero
orange_and_mango = fruits[-3:-1] # similar no incluye el ultimo elemento
orange_mango_lemon = fruits[-3:]
```
*Nota: del mismo modo aplica para la indexacion negativa intentalo tu mismo!*

## Modificar Listas
Una lista es una colección ordenada de elementos mutable o modificable. Vamos a modificar la lista de frutas.
```python
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

```
## Revisando items en Listas
Comprobar si un elemento es miembro de una lista utilizando el operador in. Véase el ejemplo siguiente.
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```
## Agregando items en una Lista
Para añadir un elemento al final de una lista existente utilizamos el método append().
```python
# Append()-(añadir al final de la lista)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)
```
## Insertando items en una Lista
Podemos utilizar el método insert() para insertar un único elemento en un índice especificado de una lista. Tenga en cuenta que los demás elementos se desplazan a la derecha. El método insert() recibe dos argumentos: el índice y el elemento a insertar.
```python
# Insert()-( añadir un elemento en una posición específica)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # inserta apple despues de banana y mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)
```
## Removiendo items de una Lista
El método remove elimina un elemento especificado de una lista
```python
# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']
```
### Removiendo items con Pop
El método pop() elimina el índice especificado, (o el último elemento si no se especifica el índice):
```python
# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 
```
### Removiendo items con Del
La palabra clave del elimina el índice especificado y también se puede utilizar para eliminar elementos dentro del rango del índice. También puede borrar la lista por completo
```python
# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```
## Limpiando items de una lista
El método clear() vacía la lista:
```python
# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []
```
## Copiar listas
Es posible copiar una lista reasignándola a una nueva variable de la siguiente manera: lista2 = lista1. Ahora, lista2 es una referencia de lista1, cualquier cambio que hagamos en lista2 también modificará la original, lista1. Pero hay muchos casos en los que no nos gusta modificar el original sino tener una copia diferente. Una forma de evitar el problema anterior es usar copy().
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```
## Union de Listas
Hay varias formas de unir, o concatenar, dos o más listas en Python.
```python
# syntax
list3 = list1 + list2

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
```
Unir usando el método extend() El método extend() permite añadir una lista a otra. Véase el siguiente ejemplo
```python
# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )
```
## Contar items de una lista
El método count() devuelve el número de veces que aparece un elemento en una lista:
```python
# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```
## Encontar el index de un elemento
El método index() devuelve el índice de un elemento de la lista:
```python
# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 
```
## Sorteando items de una Lista
Para ordenar listas podemos utilizar el método sort() o las funciones integradas sorted(). El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del método sort() reverse es igual a true, ordenará la lista en orden descendente.
```python
# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 
```
