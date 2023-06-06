# Operadores
### Booleano
Un tipo de datos booleano representa uno de los dos valores: Verdadero o Falso. El uso de estos tipos de datos quedará claro una vez que empecemos a utilizar el operador de comparación. La primera letra T para Verdadero y F para Falso deben ser mayúsculas a diferencia de JavaScript. Ejemplo: Valores booleanos
```python
print(True)
print(False)
```
## Operadores
El lenguaje Python soporta varios tipos de operadores. En esta sección, nos centraremos en algunos de ellos.

### Operadores de Asignacion
Los operadores de asignación se utilizan para asignar valores a variables. Tomemos = como ejemplo. El signo igual en matemáticas muestra que dos valores son iguales, sin embargo en Python significa que estamos almacenando un valor en una determinada variable y lo llamamos asignación o asignación de un valor a una variable. La siguiente tabla muestra los diferentes tipos de operadores de asignación en Python, tomados de [w3school](https://www.w3schools.com/python/python_operators.asp).
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/91c2e9aa-0f20-4c5a-be39-99e680892aad)
### Operadores Aritmeticos
- Suma(+): a + b
- Resta(-): a - b
- Multiplicación(*): a * b
- División(/): a / b
- Módulo(%): a % b
- División por el piso(//): a // b
- Exponenciación(**): a ** b

![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/64803867-10d9-4054-b208-6025344dea16)
**Ejemplo:Enteros**

```python
# Operadores artmetios
# Enteros

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 
```
**Ejemplo:Floats**
```python
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```
**Ejemplo:Complex numbers**
```python
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```
Vamos a declarar una variable y asignarle un tipo de dato numérico. Voy a utilizar una variable de un solo carácter, pero recuerda no desarrollar el hábito de declarar este tipo de variables. Los nombres de las variables deben ser siempre mnemotécnicos.
```python
# Declaramos la variable en la seccion superior

a = 3 # a es una variable y tiene un valor de 3
b = 2 # b es una variable y tiene un valor de 2

# Operaciones arimeticas y asignacion de resultado en variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
```
Empecemos a atar cabos y a utilizar lo que ya sabemos para calcular (área, volumen, densidad, peso, perímetro, distancia, fuerza).
```python
# Calcular el area de un circulo
radius = 10                                 # radio del circulo
area_of_circle = 3.14 * radius ** 2         # dos ** para aplicar exponente
print('Area of a circle:', area_of_circle)

# Calcular el area de un reactangulo
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calcular el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         #Agregar unidades para el peso

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density)
```
### Operadores de Comaparacion
En programación comparamos valores, utilizamos operadores de comparación para comparar dos valores. Comprobamos si un valor es mayor o menor o igual a otro valor. La siguiente tabla muestra los operadores de comparación de Python que fue tomada de [w3shool](https://www.w3schools.com/python/python_operators.asp).
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/f3b81adb-be6b-4768-9cb5-ac957ab0d8f9)
**Ejemplo de operadores de comparacion**
```python
#************************Operadores de comparacion****************************
print("************************Operadores de comparacion****************************")
print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 es mayor que 2
print(3 < 2)     # False,  porque 3 es mayor que 2
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 diferente a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

```
Además del operador de comparación anterior Python utiliza:
* is: Devuelve verdadero si ambas variables son el mismo objeto(x es y)
* is not: Devuelve verdadero si ambas variables no son el mismo objeto(x no es y)
* in: Devuelve True si la lista consultada contiene un determinado elemento(x en y)
* not in: Devuelve True si la lista consultada no contiene un determinado elemento(x en y)
```python
print('1 is 1', 1 is 1)                   # True - porque the data values are the same
print('1 is not 2', 1 is not 2)           # True - porque 1 is not 2
print('C in Cristian', 'C' in 'Cristian') # True - C esya en la cadena
print('B in Cristian', 'B' in 'Cristian') # False - Porque B no esta en la cadena
print('coding' in 'coding for all') # True - porque coding esta en coding for all
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
```

### Operadores Logicos
A diferencia de otros lenguajes de programación, python utiliza las palabras clave and, or y not para los operadores lógicos. Los operadores lógicos se utilizan para combinar sentencias condicionales:
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/100cb1a6-faa6-4ff8-8917-0e5766bd2da1)

```python
#********************************Operadores logicos**********************
print("************************Operadores logicos****************************")
print(3 > 2 and 4 > 3) # True - porque ambos argumentos son verdaros
print(3 > 2 and 4 < 3) # False - Porque el segundo argumento es falso
print(3 < 2 and 4 < 3) # False - porque ambos argumentos son falsos
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - porque ambos argumentos son verdaderos
print(3 > 2 or 4 < 3)  # True - porque uno de los argumentos es verdadero
print(3 < 2 or 4 < 3)  # False - porque ambos argumentos son falsos
print('True or False:', True or False)
print(not 3 > 2)     # False - 3 es mayor que 2,pero not invierte el resultado
print(not True)      # False - El operador Not invierte True a False y viceversa
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

Excelente! una seccion mas avanzada!,ahora toca repasar con unos ejercicios :str
## Ejercicios

* Declara tu edad como variable integer
* Declara tu altura como una variable float
* Declara una variable que almacene un número complejo
* Escribe un script que pida al usuario que introduzca la base y la altura del triángulo y calcule el área de este
triángulo (área = 0,5 x b x h)
* Escribe un script que pida al usuario que introduzca el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c)
* Obtener la longitud y la anchura de un rectángulo mediante un prompt. Calcular el área (área = largo x ancho) y el perímetro (perímetro = 2 x (largo + ancho)).
* Obtén el radio de un círculo usando el prompt. Calcular el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
* Escribe un script que pida al usuario que introduzca el número de años. Calcula el número de segundos que ha vivido la persona.
* Escribe un script en Python que muestre la siguiente tabla
```python
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

*Nota: puedes consultar el script [operadores.py](operadores.py) para mas ejemplos *
