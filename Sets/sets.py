### **Crear un conjunto**

#Usamos corchetes, {} para crear un conjunto o la función integrada *set()* .

# Crear un conjunto vacío
# syntax
st = {}
# or
st = set()

#Creación de un conjunto con elementos iniciales

# syntax
st = {'item1', 'item2', 'item3', 'item4'}


#**Ejemplo:**

# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}


### **Obtener la longitud del conjunto**

#Usamos el método **len()** para encontrar la longitud de un conjunto.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)

#**Ejemplo:**
frutas  = { 'plátano' , 'naranja' , 'mango' , 'limón' }
len ( frutas )

### **Acceder a elementos en un conjunto**

#Usamos bucles para acceder a los elementos. Veremos esto en la sección de bucle.

### **Comprobación de un artículo**

#Para verificar si existe un elemento en una lista, usamos el operador *de* membresía.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True


#**Example:**

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

### **Adición de elementos a un conjunto**

#Una vez que se crea un conjunto, no podemos cambiar ningún elemento y también podemos agregar elementos adicionales.

#- Agrega un elemento usando *add()*
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
#**Example:**
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

#• Agregar múltiples elementos usando *update()* , update*()* permite agregar múltiples elementos a un conjunto. update*()* toma un argumento de lista.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

#**Example:**

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

### **Eliminación de elementos de un conjunto**

#Podemos eliminar un elemento de un conjunto usando el método *remove()* . Si no se encuentra el elemento , el método *remove()* generará errores, por lo que es bueno verificar si el elemento existe en el conjunto dado. Sin embargo, el método *descarte ()* no genera ningún error.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

#Los métodos pop() eliminan un elemento aleatorio de una lista y devuelve el elemento eliminado.

### Ejemplo:
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

#si estamos interesados en el articulo eliminado
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

### **Borrado de artículos en un conjunto**

#Si queremos borrar o vaciar el conjunto, usamos el método de *clear.*
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

#**Example:**
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

### **Eliminación de un conjunto**

#Si queremos eliminar el conjunto en sí, usamos el operador *del*
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st


#**Example:**
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits


### **Convertir lista en conjunto**

#Podemos convertir lista en conjunto y conjunto en lista. La conversión de la lista al conjunto elimina los duplicados y solo se reservarán elementos únicos.


# sintaxis lst  = [ 'elemento1' , 'elemento2' , 'elemento3' , 'elemento4' , ' elemento1 ' ]
st = set ( lst )   # {'elemento2', 'elemento4', 'elemento1', 'elemento3'} - el orden es aleatorio, porque los conjuntos en general no están ordenados 

#**Ejemplo:**


fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}


### **Unión de conjuntos**

#Podemos unir dos conjuntos usando el método *union()* o *update()* .

#- Unión Este método devuelve un nuevo conjunto
 # syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)


#**Ejemplo:**
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

#- Actualizar Este método inserta un conjunto en un conjunto dado

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

#**Ejemplo:**

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

### **Búsqueda de elementos de intersección**

#La intersección devuelve un conjunto de elementos que están en ambos conjuntos. Ver el ejemplo

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

#**Ejemplo:**

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}


### **Comprobación de subconjunto y superconjunto**

#Un conjunto puede ser un subconjunto o superconjunto de otros conjuntos:

#- Subconjunto: *issubset()*
#- Súper conjunto: *issuperset*


# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

#**Ejemplo:**

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

### **Comprobar la diferencia entre dos conjuntos**

#Devuelve la diferencia entre dos conjuntos.
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

#**Ejemplo:**
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
### **Encontrar diferencias simétricas entre dos conjuntos**
#Devuelve la diferencia simétrica entre dos conjuntos. 
#Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, 
#excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
#**Ejemplo:**

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

### **Unión de conjuntos**

#Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos. Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el método *isdisjoint()* .

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
