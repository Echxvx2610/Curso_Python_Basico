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
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/93f88732-06d3-4885-bb0d-ad47efb5a724)

```python
#********************************* Strings en sentencia de caracteres *******************************************
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
### Invertir un String
Podemos invertir cadenas fácilmente en python,de la siguiente forma:
```python
#************************************************** Invertir una cadena **********************************************
print('************************************************** Invertir un string ***********************************')
saludo = 'Hola'
print(saludo[::-1])
```
### Saltar caracteres durante el corte
Es posible omitir caracteres durante el corte pasando el argumento step al método slice.
```python
#************************************* skip caractares en un string *******************************************
print('************************************** skip caractares en un string ****************************')
job = 'Programador'
pro = job[0:3] #seleccionamos solo los cactacteres del 0 al 3 lo demas lo skipeamos
print(pro) #skip 10 caracteres
```
## Metodos Importantes de Strings
Existen muchos métodos de cadena que nos permiten formatear cadenas. Vea algunos de los métodos de cadena en el siguiente ejemplo:

* capitalize(): Convierte el primer carácter de la cadena en mayúscula
```python
#capitalize()
carrera = 'ingenieria de sistemas' # convierte la primera letra en mayuscula
print(carrera.capitalize())
```
* count(): devuelve las ocurrencias de la subcadena en la cadena, count(substring, start=.., end=..). El inicio es un índice inicial para contar y el fin es el último índice para contar.
```python
#count() 
platillo = 'pizza' # contar cuantas veces aparece una letra
print(platillo.count('a'))
print(platillo.count('z'))
```
* endswith(): Comprueba si una cadena termina con una terminación especificada.
```python
#endswith()
bebida = "Mojito" # verifica si la cadena termina con el string o caracter deseado
print(bebida.endswith('to'))
print(bebida.endswith('sa'))
```
* expandtabs(): Sustituye el carácter de tabulación por espacios, el tamaño de tabulación por defecto es 8. Toma el argumento tamaño de tabulación
```python
#expandtabs()
dias = "Lunes\tMartes\tMiercoles\tJueves\tViernes" # aplica tabulacion o como tal extendiende una tabulacion
print(dias.expandtabs())
print(dias.expandtabs(15))
```
* find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
```python
#find()
calle = "Venustiano carranza" # retorna el index de la string o caracter a buscar(el index del primer caracter a buscar,si no encuentra el caracter, retorna -1)
print(calle.find('ca'))
```
* rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1
```python
rfind()
print(calle.rfind('za')) # similar pero prioriza en el segundo index
```
* format(): da formato a la cadena para que salga mejor
```python
#format()
nombre_f = "Cristian"
apellido_f = "Echevarria"
print("el nombre completo es {} {}".format(nombre_f, apellido_f))
```
* join(): Devuelve una cadena concatenada
```python
web_tech = "Python, Django, Flask"
result = "#".join(web_tech)
print(result)
```
* strip(): Elimina todos los caracteres dados empezando por el principio y el final de la cadena.
```python
auto = "nissan altima"
print(auto.strip("ssan")) # remueve los caracteres especificados del primero y segundo string
```
* replace(): Sustituye la subcadena por una cadena dada
```python
avion = "Boing 747"  #Remplaza un string o caracter por otro en el string original
print(avion.replace("Boing", "Boeing"))
print(avion.replace("747", "777"))
print(avion.replace(" ", "-"))
```
* split(): Divide la cadena, utilizando la cadena dada o el espacio como separador.
```python
#split()
nombre = "Cristian Echevarria"
print(nombre.split()) #separa el string en una lista
```
* swapcase(): Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a mayúsculas.
```python
#swapcase() 
moto = "ITALIKA"
print(moto.swapcase()) # convierte de mayuscula a minuscula y viceversa
moto_2 = "italika"
print(moto_2.swapcase())
```
## Ejercicios
* Concatena el string 'Curso', 'Basico', 'De', 'Python' en una sola cadena, 'Curso Basico de Python'.
* Concatena el string  'Codificación', 'Para' , 'Todos' en una sola cadena, 'Codificación Para Todos'.
* Declara una variable llamada empresa y asígnele un valor inicial "Codificación Para Todos".
* Imprime la variable empresa utilizando print().
* Imprime la longitud de la cadena empresa utilizando el método len() y print().
* Cambia todos los caracteres a mayúsculas utilizando el método upper().
* Cambia todos los caracteres a minúsculas utilizando el método lower().
* Utiliza los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Curso Basico de Python".
* Cortar la primera palabra de la cadena "Curso Basico de Python".
* "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.
* Comprueba si la cadena "Curso Basico de Python" contiene una palabra "curso" utilizando el método find u otros métodos.
* Reemplazar la palabra Curso en la cadena 'Curso para todos' por Python.
* Utilice el método de formato de cadena para mostrar lo siguiente:
```script
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```
