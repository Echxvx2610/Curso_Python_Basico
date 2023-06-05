# Introduccion a python

## 📖 Que es Python?
Guido Van Rossum, un programador de computación de los Países Bajos, creó Python. Python comenzó en 1989 en el Centrum Wiskunde & Informatica (CWI), en principio como un proyecto de afición para mantenerse ocupado durante las vacaciones de Navidad. El nombre del lenguaje se inspiró en el programa de televisión de la BBC “Monty Python’s Flying Circus” debido a que Guido Van Rossum era un gran aficionado del programa. 

## ¿Porque python? 🤔

Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning  (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo.
Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes

## ¿Qué beneficios ofrece Python?
Los beneficios de Python incluyen los siguientes:

* Los desarrolladores pueden leer y comprender fácilmente los programas de Python debido a su sintaxis básica similar a la del inglés. 
* Python permite que los desarrolladores sean más productivos, ya que pueden escribir un programa de Python con menos líneas de código en comparación con muchos otros lenguajes.
* Python cuenta con una gran biblioteca estándar que contiene códigos reutilizables para casi cualquier tarea. De esta manera, los desarrolladores no tienen que escribir el código desde cero.
* Los desarrolladores pueden utilizar Python fácilmente con otros lenguajes de programación conocidos, como Java, C y C++.
* La comunidad activa de Python incluye millones de desarrolladores alrededor del mundo que prestan su apoyo. Si se presenta un problema, puede obtener soporte rápido de la comunidad.
* Hay muchos recursos útiles disponibles en Internet si desea aprender Python. Por ejemplo, puede encontrar con facilidad videos, tutoriales, documentación y guías para desarrolladores.
* Python se puede trasladar a través de diferentes sistemas operativos de computadora, como Windows, macOS, Linux y Unix.

## Basicos de Python
Un script de Python puede ser escrito en la consola interactiva de Python o en el editor de código. Un archivo de Python tiene la extensión .py.

### Python Sheel
una vez descargado e instalado python puedo ejecutar la consola de python ejecutando el programa sig: ![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/41bcdd30-4b71-4084-8e80-f733f15f8be1), veras la siguiente consola:

![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/794e6ed9-66cf-42bb-812f-15d46dfd8806)

Prueba hacer operaciones senciillas para que te familiarices con la consola o el lenguaje,por ejemplo:
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/f117be67-d38f-432d-b0e6-e12e54f38492)

### Hola mundo! 🙋
prueba escribir en la consola:
```shell
print("Hello World!")
```
Felicidades acabas de imprimir tu primer hola mundo!✨

### Indentacion de Python
Una indentación es un espacio en blanco en un texto. La indentación en muchos lenguajes se utiliza para aumentar la legibilidad del código, sin embargo, Python utiliza la indentación para crear bloques de código. En otros lenguajes de programación, se utilizan llaves ({}), en lugar de la indentación, para crear bloques de código. Uno de los errores comunes al escribir código en Python es tener una indentación incorrecta.
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/b60a3ee5-071b-4b28-9824-513676d0c4ec)

Forma correcta:
![image](https://github.com/Echxvx2610/Curso_Python_Basico/assets/99057175/5ce24917-20d6-430a-a199-c90ebc911329)

### Comentarios
**Comentarios basicos**

Los comentarios son muy importantes para hacer que el código sea más legible y para dejar notas en nuestro código. Python no ejecuta las partes del código que son comentarios. Cualquier texto que comience con el símbolo de numeral (#) en Python se considera un comentario.
``` shell 
#Esto es un comentario
#segundo comentario
#tercer comentarios,los comentarios no son visibles en el script final solo en el codigo fuente

```
**Comentarios multilinea**
``` shell
'''
Este es un comentario mulitlinea,util para una gran descripcion o docstring
pueden crearce con comilla simple o doble comilla
'''
```
### Tipos de Datos
En Python, hay varios tipos de datos. Comenzaremos con los más comunes. Los diferentes tipos de datos se explicarán en detalle en otras secciones. Por ahora, simplemente repasaremos los diferentes tipos de datos para familiarizarnos con ellos. No es necesario tener una comprensión clara en este momento.

**Numeros**

* Integer o Enteros(Netivos y positivos asi como cero)
  * Ejemplo: -3,-2,-1,0,1,2,3 
* Float o decimales
  * Ejemplo: 2.34,3.1414,10.00
* Complex o complejos
  * Ejemplos: 1 + j,2 + 4j
 
**String**

Una cadena de caracteres es una colección de uno o más caracteres encerrados entre comillas simples o dobles. Si una cadena de texto abarca más de una oración, se utiliza comillas triples.
```shell
'Cristian'
'Echevarria'
'Adoro el cafe'
```
**Booleano**

El tipo de dato booleano en Python puede tener dos valores: True (verdadero) o False (falso). Es importante tener en cuenta que las letras "T" y "F" deben estar siempre en mayúsculas para representar los valores booleanos correctamente.
```shell
True # esta la luz prendida? si la luz esta prendida el valor es verdadero
False # esta la luz prendida? si la luz esta apagada el valor es falso
```

**Listas**

Una lista es una colección ordenada que permite almacenar elementos de diferentes tipos de datos. Una lista es similar a un arreglo en JavaScript.
Puedes crear una lista en Python utilizando corchetes [] y separando los elementos por comas. Los elementos de una lista pueden ser de cualquier tipo de datos, como enteros, cadenas, booleanos, u otros objetos.

```shell
[0, 1, 2, 3, 4, 5]  # lista del mismo tipo de dato(numero)
['Banana', 'Orange', 'Mango', 'Avocado'] # lista del mismo tipo de dato(string)
['Finland','Estonia', 'Sweden','Norway'] # lista del mismo tipo de dato(string)
['Banana', 10, False, 9.81] # Lista de diferentes tipos de datos (string, integer, boolean y float)
```
**Tuplas**

Una tupla es una colección ordenada de diferentes tipos de datos, al igual que una lista. Sin embargo, a diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez que se han creado.

```shell
('Cristian', 'Oscar', 'Israel', 'Felix', 'Malcara') # Nombres
```
**Set**

Un conjunto (set) es una colección de tipos de datos similar a una lista o una tupla. Sin embargo, a diferencia de las listas y las tuplas, un conjunto no es una colección ordenada de elementos. Además, al igual que en matemáticas, un conjunto en Python solo almacena elementos únicos, eliminando automáticamente cualquier duplicado.

```shell
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # el orden no es importante en los sets
```
**Diccionarios**

un diccionario es un objeto que representa una colección desordenada de datos en un formato de pares clave-valor. Cada elemento en un diccionario consiste en una clave (key) y su respectivo valor (value).
Los diccionarios en Python se definen utilizando llaves {} y los pares clave-valor se separan por dos puntos (:). Los elementos en un diccionario no tienen un orden específico.
```shell
{
'first_name':'Cristian',
'last_name':'Echevarria',
'country':'Mexico', 
'age':21, 
'is_married':False,
'skills':['Python', 'MySQL', 'HTML', 'CSS']
}
```

## Revsiar el tipo de dato

Para reviar el tipo de dato de un dato podemos usar la funcion integrada de python *type()*
```shell
print(type("Hello world!"))
```

## Comencemos en Visual Studio Code

Abre tu Visual Studio Code, crea un archivo llamado helloword.py
La consola interactiva de Python imprimía sin usar "print", pero en Visual Studio Code, para ver nuestros resultados, debemos usar la función incorporada *print(). La función print() toma uno o más argumentos de la siguiente manera: print('argumento1', 'argumento2', 'argumento3'). A continuación, puedes ver ejemplos:
```shell
#Introduccion

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

```
### Ejercicios

* Revisa en consola la version de python que estas usando
* En la consola python realiza al menos una operacion con cada uno de los operadores.
  * addition(+)
  * subtraction(-)
  * multiplication(*)
  * modulus(%)
  * division(/)
  * exponential(**)
  * floor division operator(//)
* Escribe las siguientes string en la consola:
  * nombre
  * apellido
  * pais
  * Algo que te guste hacer
* Revisa el tipo de dato de los siguientes datos:
  * 10
  * 9.8
  * 3.14
  * 4 - 4j
  * ['Cristian', 'Python', 'Sistemas']
  * Tu nombre
  * Tu apellido
  * Tu pais

## Extra

Crea un folder llamado Curso_Basico_python dentro de ella crea una carpeta llamada introduccion y realiza los ejercicios en la app visual studio code.
vera algo similar a [helloword.py](helloword.py), como recomendacion crea una capeta por cada tema visto. Suerte!!
