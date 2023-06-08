# Strings (Cademas de texto)
Texto es un tipo de datos de cadena. Cualquier tipo de dato escrito como texto es una cadena. Cualquier dato entre comillas simples, dobles o triples es una cadena. Existen diferentes métodos de cadena y funciones incorporadas para tratar con tipos de datos de cadena. Para comprobar la longitud de una cadena utilice el método len().
```python
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
print(sentence)             # Espero que estes disfrutando este curso
```
La cadena multilínea se crea utilizando comillas simples triples (''') o comillas dobles triples ("""). Véase el ejemplo siguiente.
```python
#************************************* Multilineas  *************************************************************
print('************************************* Multilineas  *************************************************************')
#La cadena multilínea se crea usando comillas triples simples (''') o triples dobles (""").
multiline_string = '''Soy un estudiante de ingnieria en sistemas computacionales 
y estoy creando un curso de Python.'''
print(multiline_string)

# otra forma de hacer lo mismo
multiline_string = """Soy un estudiante de ingnieria en sistemas computacionales 
y estoy creando un curso de Python."""
print(multiline_string)
```
## Concatenacion de Strings
Podemos conectar cadenas entre sí. La unión o conexión de cadenas se denomina concatenación. Vea el ejemplo siguiente:
```python
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
```

## Escape de secuencia con strings
En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

\n: nueva línea
\t: Tabulador (8 espacios)
\t: Tabulador significa(8 espacios)
\': Comilla simple (')
\": Comilla doble (")
Veamos ahora el uso de las secuencias de escape anteriores con ejemplos.
```python
# Secuencias de escape en cadenas
print('Espero que estes disfrutando este curso.\nlo estas? ?')
print('Days\tTopics\tExercises') # Agregando tabulacion entre cadenas
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('Este es el simbolo de backslash (\\)') # \
print('Cada que programo con un lenguaje nuevo escribo: \"Hello, World!\"') # to write a double quote inside a single quote

```
## Formato de Strings
Formato antiguo de cadenas (operador %)
En Python hay muchas formas de formatear cadenas. En esta sección, cubriremos algunas de ellas. El operador "%" se usa para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con "especificadores de argumento", símbolos especiales como "%s", "%d", "%f", "%.número de dígitosf".

%s - Cadena (o cualquier objeto con una representación de cadena, como números)
%d - Números enteros
%f - Números de coma flotante
"%.number of digitsf" - Números de coma flotante con precisión fija
```python
# **************************************** Formato de cadenas *********************************************************
print('************************************ Formato de cadenas *********************************************************')
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
```
### Nuevo estilo de Formato de Strings
*Este formato fue introduccido desde la version Python v3.0
```python
#************************************ Nuevo formato de cadenas *********************************************************
print('****************************** Nuevo formato de cadenas *********************************************************')
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
```
## Strings y Secuencia de Caracteres
Las cadenas de Python son secuencias de caracteres, y comparten sus métodos básicos de acceso con otras secuencias ordenadas de objetos de Python: listas y tuplas. La forma más sencilla de extraer caracteres individuales de las cadenas (y miembros individuales de cualquier secuencia) es descomprimirlos en las variables correspondientes.
```python#********************************* Strings en sentencia de caracteres *******************************************
print('************************************ Strings en sentencia de caracteres ***************************************')
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
```
### Acceder a los elementos de un string via index
En programación, la cuenta empieza por cero. Por lo tanto, la primera letra de una cadena está en el índice cero y la última letra de una cadena es la longitud de una cadena menos uno.
```python
#********************************** Acceso a caracteres en una string por medio de index *********************************
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

```

