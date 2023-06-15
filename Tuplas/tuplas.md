# Tuplas
Una tupla es una colección de diferentes tipos de datos ordenados e inmutables. Las tuplas se escriben con corchetes, (). Una vez creada una tupla, no podemos cambiar sus valores. No podemos utilizar los métodos add, insert, remove en una tupla porque no es modificable (mutable). A diferencia de las listas, las tuplas tienen pocos métodos. Métodos relacionados con las tuplas:

* tuple(): para crear una tupla vacía
* count(): para contar el número de un elemento especificado en una tupla
* index(): para encontrar el índice de un elemento especificado en una tupla
* operator: para unir dos o más tuplas y crear una nueva tupla

## Creando una tupla
* tupla vacia: Crear una tupla vacia
```python
# syntax
empty_tuple = ()
# o usando el constructor de tuplas
empty_tuple = tuple()
```
* tupla con valores iniciales
```python
fruits = ('banana', 'orange', 'mango', 'lemon')
```
## Largo de una tupla
podemos usar el metodo len() para revisar el largo u tamaño de una tupla
```python
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl) # 3
```
## Accesando a los elementos de una tupla
Indexación positiva De forma similar al tipo de datos lista, utilizamos la indexación positiva o negativa para acceder a los elementos de las tuplas.
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/c5cf4245-b49b-4073-aa40-5c07c0abd59a)
```python
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[las_index]
```
Indexación negativa La indexación negativa significa que empezando por el final, -1 se refiere al último elemento, -2 al penúltimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/d95d70d0-0cb6-47a9-ada9-e4e11e69cdc9)
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```
## Cortando tuplas
Podemos trocear una sub-tupla especificando un rango de índices donde empezar y donde terminar en la tupla, el valor de retorno será una nueva tupla con los elementos especificados.
* Rango de indices positivo 
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # Todos los items
all_fruits= fruits[0:]      # Todos los items
orange_mango = fruits[1:3]  # No incluye el item 3
orange_to_the_rest = fruits[1:]
```
* Rangoa de índices negativos
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # todos los items
middle_two_items = tpl[-3:-1]  # no incluye el item 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # todos los items
orange_mango = fruits[-3:-1]  # no inluye el item 3
orange_to_the_rest = fruits[-3:]
```
## Cambiar una tupla a una lista
Podemos cambiar tuplas a listas y listas a tuplas. las tuplas son inmutables si queremos modificar una tupla debemos cambiarla o convertirla en una lista para editarla y al final podemos regresarla de nuevo a una tupla.
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon') #declaramos una tupla
fruits = list(fruits) #a la convertimos a lista
fruits[0] = 'apple' # editamos el elemento de la posicion 0, de banana a apple
print(fruits)     # ['apple', 'orange', 'mango', 'lemon'] #notese el cambio
fruits = tuple(fruits) #la convertimos a tupla de nuevo
print(fruits)     # ('apple', 'orange', 'mango', 'lemon') # y asi editamos una tupla
```
## Revisar elementos en una tupla
Podemos comprobar si un elemento existe o no en una tupla utilizando in, devuelve un booleano.
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```
## Unir tuplas
Podemos unir dos o más tuplas utilizando el operador +.
```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```
## Eliminando tuplas
No es posible eliminar un único elemento de una tupla, pero sí es posible eliminar la propia tupla utilizando del.
```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```
*Nota: recuerda que puedes hacer cualquier operacion con las tuplas siempre y cuando la conviertas a una lista y la regreses a tupla,pero ten en cuenta las caracteristicas de una tupla antes de convertirla a lista y viceversa*


## Ejercicios
* Crear una tupla vacía
* Crea una tupla que contenga los nombres de tus hermanos y hermanas (hermanos imaginarios si no tienes hermanos)
* Une las tuplas hermanos y hermanas y asígnalo a hermanos
* ¿Cuántos hermanos tienes?
* Modifica la tupla hermanos y añade el nombre de tu padre y de tu madre y asígnalo a family_members
* Desempaquetar hermanos y padres de family_members
* Crea las tuplas frutas, verduras y productos animales. Unir las tres tuplas y asignarlas a una variable llamada
food_stuff_tp.
* Cambiar la tupla sobre food_stuff_tp a una lista food_stuff_lt
* Extraiga el elemento o elementos centrales de la tupla food_stuff_tp o de la lista food_stuff_lt.
* Elimine los tres primeros y los tres últimos elementos de la lista food_stuff_lt.

*Nota: para consultar notas o dudad puedes revisar el archivo [tuplas.py](./tuplas.py)
