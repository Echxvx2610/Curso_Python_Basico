# Sets (conjuntos) 
Conjunto es una colección de elementos. Permíteme que te recuerde tus clases de matemáticas de primaria o secundaria. La definición matemática de conjunto se puede aplicar también en Python. Conjunto es una colección de elementos distintos desordenados y no indexados. En Python el conjunto se utiliza para almacenar elementos únicos, y es posible encontrar la unión, intersección, diferencia, diferencia simétrica, subconjunto, superconjunto y conjunto disjunto entre conjuntos.
## Creación de un conjunto
Utilizamos llaves {} para crear un conjunto o la función incorporada set().
* Creación de un conjunto vacío
```python
# syntax
st = {}
# or
st = set()
```
* Crear un conjunto con items
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```
## Obtención de la longitud del conjunto
podemos utilizar la funcion integrada len() para medir el tamaño o largo de un set
```python
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))
```
**Ejemplo**
```python
frutas = {"Fresa"."Platano","naranja","Manzana"}
print(len(frutas))
```
## Acceso a Elementos de un Conjunto
Utilizamos bucles para acceder a los elementos. Lo veremos en la sección de bucles
### Comprobación de un elemento
Para comprobar si un elemento existe en una lista se utiliza el operador de pertenencia.
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("En el conjunto se encuentra el item3?", 'item3' in st) # verdadero!
```
**Ejemplo**
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```
## Adición de elementos a un conjunto
Una vez creado un conjunto, no podemos cambiar ningún elemento y también podemos añadir elementos adicionales.
* Apregar un item usando add()
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```
**Ejemplo**
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```
* Agregar multiples elementos usando update(), toma una lista de argumentos y los agrega al conjunto
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```
**Ejemplo**
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```
## Borrado de elementos de un conjunto
Podemos eliminar un elemento de un conjunto utilizando el método remove(). Si el elemento no se encuentra, el método remove() generará errores, por lo que es bueno comprobar si el elemento existe en el conjunto dado. Sin embargo, el método discard() no genera ningún error.
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```
Los métodos pop() eliminan un elemento aleatorio de una lista y devuelve el elemento eliminado.
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
```
## Eliminación de un conjunto
Si queremos borrar nuestro conjunto podemos hacer uso del operador *del()*
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```
## Conversión de lista en conjunto
Podemos convertir lista en conjunto y conjunto en lista. La conversión de lista a conjunto elimina los duplicados y sólo se reservarán los elementos únicos.
```python
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} -el orden es aleatoria ya que normalmente asi lo es
```
**Ejemplo**
```python
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```
## Unión de Conjuntos
Podemos unir dos conjuntos utilizando el método union() o update().
* Unión Este método devuelve un nuevo conjunto
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```
**Ejemplo**
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```
* Actualizar Este método inserta un conjunto en un conjunto dado
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```
**EJemplo**
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```
## Búsqueda de elementos de intersección
La intersección devuelve un conjunto de elementos que se encuentran en ambos conjuntos.
**Ejemplo**
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```
**EJemplo**
```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```
## Comprobación de la diferencia entre dos conjuntos
Devuelve la diferencia entre dos conjuntos.
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```
**Ejemplo**
```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```
## Búsqueda de la diferencia simétrica entre dos conjuntos
Devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A)
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```
**Ejemplo**
```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```
## Union de conjuntos
Si dos conjuntos no tienen un elemento o elementos comunes los llamamos conjuntos disjuntos. Podemos comprobar si dos conjuntos son conjuntos o disjuntos utilizando el método isdisjoint().
```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```
**Ejemplo**
```python
even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
```

## Ejercicios
```python
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```
* Encontrar la longitud del conjunto it_companies
* Añadir 'Twitter' a it_companies
* Insertar varias empresas de TI a la vez en el conjunto it_companies
* Eliminar una de las empresas del conjunto it_companies
* ¿Cuál es la diferencia entre eliminar y descartar?
* Unir A y B
* Buscar A intersección B
* Es A subconjunto de B?
* ¿Son A y B conjuntos disjuntos?
* Unir A con B y B con A
* Cuál es la diferencia simétrica entre A y B
* Eliminar los conjuntos completamente

