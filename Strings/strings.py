# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 18:02:06 2021
@Author: Cristian A. Echevarria
"""
#*********************************************** Strings *********************************************************
print('*********************************************** Strings *********************************************************')
#Ejemplos de strings (cadenas), para mas info revisar apuntes de notion
letter = 'P'                # A string puede ser un caracter o una serie de caracteres
print(letter)               # P
print(len(letter))          # 1 medido el tamaño de la cadena
greeting = 'Hello, World!'  # String puede escribirse con comillas simples o dobles: "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "Espero que estes disfrutando este curso"
print(sentence)             #I hope you are enjoying 30 days of Python Challenge

#************************************* Multilineas  *************************************************************
print('************************************* Multilineas  *************************************************************')
#La cadena multilínea se crea usando comillas triples simples (''') o triples dobles (""").
multiline_string = '''Soy un estudiante de ingnieria en sistemas computacionales 
y estoy creando un curso de Python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """Soy un estudiante de ingnieria en sistemas computacionales 
y estoy creando un curso de Python."""
print(multiline_string)
# ************************************************* Concatenacion *********************************************************
print('************************************************* Concatenacion *********************************************************')
#Podemos conectar strngs juntarlos,combinar o conectar cadenas a esto se le llama concatenación. 
first_name = 'Cristian'
last_name = 'Echevarria'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Cristian Echevarria
# Revisando el largo de las strings con la funcion len()
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

# Secuencias de escape en cadenas
print('Espero que estes disfrutando este curso.\nlo estas? ?')
print('Days\tTopics\tExercises') # Agregando tabulacion entre cadenas
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('Este es el simbolo de backslash (\\)') # \
print('Cada que programo con un lenguaje nuevo escribo: \"Hello, World!\"') # to write a double quote inside a single quote


# ********************************************** Formato de cadenas *********************************************************
print('********************************************** Formato de cadenas *********************************************************')
#Formato viejo/ El operador "%" se usa para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con "especificadores de argumento", símbolos especiales como "%s" , "%d", "%f", "%.número de dígitos".

# Strings only
first_name = 'Cristian'
last_name = 'Echevarria'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El area de un circulo con un radio de %d es %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string) #"The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

#********************************************** Nuevo formato de cadenas *********************************************************
print('********************************************** Nuevo formato de cadenas *********************************************************')
#nuevo estilo de formato string
first_name = 'Cristian'
last_name = 'Echevarria'
food = 'Pizza'
new_formated_string = 'I am {} {}. I love the {}'.format(first_name, last_name, food)
print(new_formated_string)

a = 10
b = 20

print('%d + %d = %d' %(a, b, a+b)) #estilo de formato obsolto pero funcional
print('{} + {} = {}'.format(a, b, a+b)) #estilo de formato nuevo pero funcional
print('{} - {} = {}'.format(a, b, a-b)) 
print("{} * {} = {}".format(a, b, a*b))
#...... puedes intentarlo con los otros operadores aritmeticos

radio = 10
PI = 3.14
area = PI * radio ** 2
c_formated_string = 'El area de un circulo con un radio de {} es {:.2f}.'.format(radio, area) # 2 refers the 2 significant digits after the point
print(c_formated_string)

#********************************************** Strings en sentencia de caracteres *********************************************************
print('******************************************* Strings en sentencia de caracteres ********************************************')
#declaras el string
fruta = 'Manzana'
#desempacas o asignas cada caracter la string manzana en una variable
a,b,c,d,e,f,g = fruta
print(a) #imprimir el primer caracter
print(b) #imprimir el segundo caracter
print(c) #imprimir el tercer caracter
print(d) #imprimir el cuarto caracter
print(e) #imprimir el quinto caracter
print(f) #imprimir el sexto caracter 
print(g) #imprimir el septimo caracter

#********************************************** Acceso a caracteres en una string por medio de index *********************************************************
print('*********************************** Acceso a caracteres en una string por medio de index ************************')
verdura = "Tomate"
primera_letra = verdura[0]
print(primera_letra)
segunda_letra = verdura[1]
print(segunda_letra)
tercera_letra = verdura[2]
print(tercera_letra)
print(verdura[3])
print(verdura[4])
print(verdura[5])

#Si queremos comenzar desde el final entonces utilizamos un index negativo comenzando desde -1
print('**************************** Acceso a caracteres en una string por medio de index(invertido)*******************')
print(verdura[-1])
print(verdura[-2])
print(verdura[-3])
print(verdura[-4])
print(verdura[-5])
print(verdura[-6])

#************************************************** Invertir una cadena ****************************************************
print('************************************************** Invertir un string ***********************************')
saludo = 'Hola'
print(saludo[::-1])

#************************************************** skip caractares en un string ****************************************************
print('************************************** skip caractares en un string ****************************')
job = 'Programador'
pro = job[0:3] #seleccionamos solo los cactacteres del 0 al 3 lo demas lo skipeamos
print(pro) #skip 10 caracteres

#***************************************** Metodos utiles en strings ****************************************************
print('****************************** Metodos utiles en strings ****************************')
#capitalize()
carrera = 'ingenieria de sistemas' # convierte la primera letra en mayuscula
print(carrera.capitalize())

#count() 
platillo = 'pizza' # contar cuantas veces aparece una letra
print(platillo.count('a'))
print(platillo.count('z'))

#endswith()
bebida = "Mojito" # verifica si la cadena termina con el string o caracter deseado
print(bebida.endswith('to'))
print(bebida.endswith('sa'))

#expandtabs()
dias = "Lunes\tMartes\tMiercoles\tJueves\tViernes" # aplica tabulacion o como tal extendiende una tabulacion
print(dias.expandtabs())
print(dias.expandtabs(15))

#find()
calle = "Venustiano carranza" # retorna el index de la string o caracter a buscar(el index del primer caracter a buscar,si no encuentra el caracter, retorna -1)
print(calle.find('ca'))

#rfind()
print(calle.rfind('za')) # similar pero prioriza en el segundo index

#format()
nombre_f = "Cristian"
apellido_f = "Echevarria"
print("el nombre completo es {} {}".format(nombre_f, apellido_f))

#joint()
web_tech = "Python, Django, Flask"
result = "#".join(web_tech)
print(result)

#strip()
auto = "nissan altima"
print(auto.strip("ssan")) # remueve los caracteres especificados del primero y segundo string

#replace()
avion = "Boing 747"  #Remplaza un string o caracter por otro en el string original
print(avion.replace("Boing", "Boeing"))
print(avion.replace("747", "777"))
print(avion.replace(" ", "-"))

#split()
nombre = "Cristian Echevarria"
print(nombre.split()) #separa el string en una lista

#swapcase() 
moto = "ITALIKA"
print(moto.swapcase()) # convierte de mayuscula a minuscula y viceversa
moto_2 = "italika"
print(moto_2.swapcase())
