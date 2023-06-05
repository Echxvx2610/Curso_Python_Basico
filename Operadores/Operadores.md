# Operadores
## Booleano
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

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
```
