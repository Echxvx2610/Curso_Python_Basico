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

