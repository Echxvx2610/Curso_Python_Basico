#Practicaremos algunas de las funciones integrada (build-in-funtions) mas comunmente usadas
from operator import truediv

#antes de empezar, recuerda que de no correr todo el codigo en visual code studio puedes abrir el sheel de phyton y practicar estos conceptos


print("hello word")           #esta imprime el texto dentro de las comillas
len('hello word')              #esta funcion cuenta el numero de caracteres dentro del parentesis incluyendo el espacio
type('helo word')               #esta nos dice que tipo de dato es el que esta leyendo
str(15)                          #convierte numeros en string
int(8)                           #convierte string en numeros
float(15)                         # convierte numeros integrales en decimales
input('Enter your name')           #toma entradas de usarios, ejemplo pregunta y respuesta etc
#Mas ejemplos de funciones

help('keywords') #imprime todas las palabras reservadas de phyton
help(str) # da informacion sobre str, puede usarse con cualquier funcion
dir(str) # da informacion sobre strin,lo mismo para cualquier funcion

#Mas ejemplos de funciones

min(20 ,30 ,40 ,50) #nos da el valor minimo
max(20 ,30 ,40, 50, 60) # nos da el valor maximo

min ([ 20, 30, 40, 40 ,70]) #toma una lista de argumentos y nos regresa el minimo
max([20,30 , 30,40,50,90]) # toma una lista de argumentos y nos regresa el valor maximo

sum([20,30,40,50]) #toma una lista de argumentos y nos regresa la suma

#*************************variables de phyton*******************

first_name = 'Cristian'
last_name = 'Echevarria'
country= 'Mexico' 
city= 'Ensenada'
age = 20 
is_married = True
skills = ['HTML', 'CSS', 'Phyton']
person_info = {
     'firstname':'Cristian',
     'lastname':'Echevarria',
    'country':'Mexico',
     'city':'Ensenada'}
     
# ********************declarar multiples variables en una linea****************************

# first_name, last_name, country, age, is_married = 'Cristian', 'Echevarria', 'Mexico', 20, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)
#*************************************************************************************************


#usemos las funciones integradas print() y len()

print('Hola mundo') #imprime nuestros argumentos
print('Hola', "si", 'no se') # puede tomar multiples argumentos
print ( len ('Hola, mundo')) #toma un argumento

# imprimamos y encontremos la longitud de las varibles
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Obtener la entrada del usuario usando la función incorporada input() . Asignemos los datos que obtenemos de un usuario a las variables first_name y age. recuerda que puedes usar el phyton sheel para probar los codigos

first_name = input('cual es tu nombre: cristian ')
age = input('cuantos anos tienes xd? 20 ')
print(first_name)
print(age)

# ****************** Comprobar los tipos de datos y conversion (con la funcion type() )*******************

# Different python data types
# Let's declare variables with various data types

first_name = 'Ivon '     # str
last_name = 'Esmeralda'       # str
country = 'Mexico'         # str
city= 'Ensenada'            # str
age = 21               # int, it is not my real age, don't worry about it

# Printing out types
print(type('Ivon'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Ivon','age':21, 'is_married': 'si'}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set


# *********** //Casting// ****************************** 
# se usa para convertir un tipo de dato en otro

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


'''
Ejercicios propuestos:

Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
'''