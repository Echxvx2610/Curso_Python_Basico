'''
Tuplas
Una tupla es una colección de diferentes tipos de datos ordenados e inmutables. Las tuplas se escriben con corchetes, (). Una vez creada una tupla, no podemos cambiar sus valores. No podemos utilizar los métodos add, insert, remove en una tupla porque no es modificable (mutable). A diferencia de las listas, las tuplas tienen pocos métodos. Métodos relacionados con las tuplas:

tuple(): para crear una tupla vacía
count(): para contar el número de un elemento especificado en una tupla
index(): para encontrar el índice de un elemento especificado en una tupla
operator: para unir dos o más tuplas y crear una nueva tupla
'''
#Creando una tupla
# syntax
empty_tuple = ()
# o usando el constructor de tuplas
empty_tuple = tuple()
tupla con valores iniciales
fruits = ('banana', 'orange', 'mango', 'lemon')

#Largo de una tupla
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl) # 3

#Accesando a los elementos de una tupla
#Indexacion Positiva
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[las_index]


#Indexacion negativa
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

#Cortando tuplas
#Rango de indices positivo
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

#Rangos de índices negativos
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # todos los items
middle_two_items = tpl[-3:-1]  # no incluye el item 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # todos los items
orange_mango = fruits[-3:-1]  # no inluye el item 3
orange_to_the_rest = fruits[-3:]

#Cambiar una tupla a una lista
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon') #declaramos una tupla
fruits = list(fruits) #a la convertimos a lista
fruits[0] = 'apple' # editamos el elemento de la posicion 0, de banana a apple
print(fruits)     # ['apple', 'orange', 'mango', 'lemon'] #notese el cambio
fruits = tuple(fruits) #la convertimos a tupla de nuevo
print(fruits)     # ('apple', 'orange', 'mango', 'lemon') # y asi editamos una tupla

#Revisar elementos en una tupla
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#Unir tuplas
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#Eliminando tuplas
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
