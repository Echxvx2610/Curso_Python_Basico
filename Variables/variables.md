# Variables y Funciones integradas (Built-in funtions)

## Funciones integradas introduccion
En Python, tenemos muchas funciones integradas. Las funciones integradas están disponibles globalmente para su uso, lo que significa que puedes utilizarlas sin importar o configurar nada. Algunas de las funciones integradas de Python más comúnmente utilizadas son las siguientes: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help() y dir(). En la siguiente tabla verás una lista exhaustiva de las funciones integradas de Python extraídas de la [documentacion oficial de python](https://docs.python.org/3/)
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/3e1c0f97-9aa6-44bf-8149-92114dcb0560)

Habramos la consola python o visual studio y provemos algunas funciones integradas
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/c32f580e-9464-4bec-9241-ef3b93b887f3)
Probemos usar dir() para ver mas informacion sobre una funcion
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/2c6b6021-6c75-4b7f-9b03-210e480417aa)
## Variables
Las variables almacenan datos en la memoria de una computadora. Se recomienda utilizar variables nemotécnicas en muchos lenguajes de programación. Una variable nemotécnica es un nombre de variable que se puede recordar y asociar fácilmente. Una variable se refiere a una dirección de memoria en la que se almacenan datos. No se permiten números al principio, caracteres especiales ni guiones al nombrar una variable. Una variable puede tener un nombre corto (como x, y, z), pero se recomienda encarecidamente usar un nombre más descriptivo (nombre, apellido, edad, país).

**Reglas para nombrar variables en Python:**

- El nombre de una variable debe comenzar con una letra o el carácter de subrayado.
- El nombre de una variable no puede comenzar con un número.
- El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _).
- Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME son variables diferentes).

Veamos unos ejemplos de como se deben declarar las variables:
```sheel
fisrtname
lastname
age
country
birth_day
num1
num2
```
nombres invalidos para una variable:
```
1num
2num
num-1
FisrtN@me
Fir$tN@me
first-name
```
Utilizaremos el estilo de nombramiento de variables estándar de Python, que ha sido adoptado por muchos desarrolladores de Python. Los desarrolladores de Python utilizan la convención de nombramiento de variables snake case (snake_case). Utilizamos el carácter de subrayado después de cada palabra para una variable que contiene más de una palabra (por ejemplo, first_name, last_name, engine_rotation_speed). El ejemplo a continuación muestra un ejemplo de nombramiento estándar de variables, donde el guion bajo es necesario cuando el nombre de la variable tiene más de una palabra.

Cuando asignamos un cierto tipo de dato a una variable, se llama declaración de variable. Por ejemplo, en el ejemplo a continuación, mi nombre de pila se asigna a una variable llamada first_name. El signo igual es el operador de asignación. Asignar significa almacenar datos en la variable. El signo igual en Python no representa igualdad como en Matemáticas.

**Ejemplo:**
```python
first_name = "Cristian"
last_name = "Echevarria"
pais = "Mexico"
skills = ["Python","MySQL","HTML","CSS"]
```
Utilicemos las funciones integradas print() y len(). La función print() acepta un número ilimitado de argumentos. Un argumento es un valor que se puede pasar o colocar dentro de los paréntesis de la función, como se muestra en el ejemplo a continuación.

```python
print('Hello, World!') # El texto Hello world es un argumento
print('Hello',',', 'World','!') # tambien puede tomar multiples argumentos,en este caso 4
print(len('Hello, World!')) # y en este caso solo toma un argumento
```
Ahora con uso de la funcion len() veamos cual es el largo o tamaño de nuestras variables
```python
# Imprimiendo los valores almacenados en las variables

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
```

## Declarar multiples variables en una linea
**Ejemplo:**
```python
first_name, last_name, country, age, is_married = 'Cristian', 'Echevarria', 'Mexico', 21, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```
## Tomar datos de usuario
Para obtener la entrada del usuario utilizando la función integrada input(), podemos asignar los datos que obtenemos del usuario a las variables first_name y age. 

**Ejemplo:**
```python
primer_nombre = input("Cual es tu nombre? ")
edad = input("Cual es tu edad? ")
print(primer_nombre)
print(age)
```
## Tipos de datos y conversiones
En Python, hay varios tipos de datos. Para identificar el tipo de datos, utilizamos la función integrada type(). Me gustaría pedirte que te centres en comprender muy bien los diferentes tipos de datos. Cuando se trata de programación, todo se trata de tipos de datos. Introduje los tipos de datos al principio y vuelvo a mencionarlos porque cada tema está relacionado con los tipos de datos. Cubriremos los tipos de datos con más detalle en sus respectivas secciones😄.

**Revisar los tipos de datos**
```python
# Diferentes tipos de datos
# Declaremos algunas variables con diferentes tipos de datos

first_name = 'Cristian'      # str
last_name = 'Echevarria'     # str
country = 'Mexico'           # str
city= 'Ensenada'             # str
age = 21                     # int

# Imprimir diferentes tipos de datos
print(type('Crsitian'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Crsitian','age':21, 'is_married':True}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

```
**Casting:**
Convertir un tipo de datos a otro tipo de datos. Utilizamos las funciones int(), float(), str(), list(), set() para realizar conversiones de tipo. Cuando realizamos operaciones aritméticas, los números representados como cadenas de texto deben convertirse primero a int o float, de lo contrario, se producirá un error. Si deseamos concatenar un número con una cadena, el número debe convertirse primero a una cadena. Hablaremos sobre la concatenación en la sección de cadenas.
```python
# int a float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float a int
gravity = 9.81
print(int(gravity))             # 9

# int a str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str a int a float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str a list
first_name = 'Cristian'
print(first_name)               # 'Cristian'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

```
Excelente! terminaste la seccion de variables!,es hora de practicar lo aprendido y realizar algunos ejercicios.

### Ejercicios
* Declarar una variable para el primer nombre y asignarle un valor
* Declarar una variable para el apellido y asignarle un valor
* Declarar una variable para el nombre completo y asignarle un valor
* Declarar una variable para el país y asignarle un valor
* Declarar una variable para la ciudad y asignarle un valor
* Declarar una variable para la edad y asignarle un valor
* Declarar una variable para el año y asignarle un valor
* Declarar una variable para el estado civil y asignarle un valor
* Declarar una variable para un valor booleano y asignarle un valor
* Declarar una variable para el estado de la luz y asignarle un valor
* Declarar múltiples variables en una sola línea

### Extras
* Verificar el tipo de datos de todas las variables usando la función incorporada type()
* Usar la función len() para obtener la longitud del primer nombre
* Comparar la longitud del primer nombre y el apellido
* Declarar las variables num_one y num_two
* Sumar num_one y num_two y asignar el valor a la variable total
* Restar num_two de num_one y asignar el valor a la variable diff
* Multiplicar num_two y num_one y asignar el valor a la variable product
* Dividir num_one entre num_two y asignar el valor a la variable division
* Obten el primer nombre, apellido, país y edad del usuario utilizando la función incorporada input() y almacena los valores en las variables correspondientes.

*Nota:puedes consultar el script [variables.py](.variables.py) para ver mas ejemplos*


























