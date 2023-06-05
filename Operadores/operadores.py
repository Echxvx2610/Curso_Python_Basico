# Arithmetic Operations in Python
# Integers (ejemplos de enteros)

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  Regresa el resultado sin la parte decimal
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponential: ', 2 ** 3) # 8
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers (numeros complejos)
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# ********************* Declarar una variable para operar con ella **********************
#Ejemplo1

a = 3 # A es variable y tiene un valor de 3
b = 2 # B es variable y tiene un valor de 2

# Operaciones aritmeticas y asignar el resultado a una variable
print("************************ Operadores aritmeticos ****************************")
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#Ejemplo2
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declarar variables
num_one = 3
num_two = 4

# operadores aritmeticos
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#Empecemos a conectar los puntos y empecemos a hacer uso de lo que ya sabemos para calcular (área, volumen, densidad, peso, perímetro, distancia, fuerza).

# Calcular el área de un círculo
radius = 10                                 # Radio del círculo
area_of_circle = 3.14 * radius ** 2         # dos ** para elevar al cuadrado
print('Area of a circle:', area_of_circle)

# Calcular el área de un rectángulo
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calcular el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calcular la densidad de un liquido
mass = 75 # em kg
volume = 0.075 # en m^3
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3')
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


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

#In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                   # True - porque the data values are the same
print('1 is not 2', 1 is not 2)           # True - porque 1 is not 2
print('C in Cristian', 'C' in 'Cristian') # True - A found in the string
print('B in Cristian', 'B' in 'Cristian') # False - there is no uppercase B
print('coding' in 'coding for all') # True - porque coding esta en coding for all
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

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
