# Para entender al cien por cien los bucles for, y como Python fue diseñado como lenguaje de programación, 
# es muy importante entender los conceptos de iterables e iteradores.

# Son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. 
# Si piensas en un array (o una list en Python), podemos indexarlo con lista[1] por ejemplo, por lo que sería un iterable. 

# Como hemos comentado, los iterables son objetos que pueden ser iterados o accedidos con un índice. 
# Algunos ejemplos de iterables en Python son las listas, tuplas, cadenas o diccionarios. 
# Sabiendo esto, lo primero que tenemos que tener claro es que en un for, 
# lo que va después del in deberá ser siempre un iterable.

# for <variable> in <iterable>:
#     <código>

# Tiene bastante sentido, porque si queremos iterar una variable, esta variable debe ser iterable, todo muy lógico. 
# Pero llegados a este punto, tal vez de preguntes ¿pero cómo se yo si algo es iterable o no?. 
# Bien fácil, con la siguiente función isinstance() podemos saberlo. 
# No te preocupes si no entiendes muy bien lo que estamos haciendo, fíjate solo en el resultado, True significa que es iterable y False que no lo es.

# EJEMPLO:

# DATOS DE ENTRADA:

from collections.abc import Iterable
lista = [1, 2, 3, 4]
string = "Python"
number = 10

print(isinstance(lista, Iterable))
print(isinstance(string, Iterable))
print(isinstance(number, Iterable))

# DATOS DE SALIDA:

# lista = True.
# string = True.
# number = False.

# Por lo tanto las listas (list) y las cadenas (string) son iterables, pero la variable 'number', que es un entero (int) no lo es. 
# Es por eso por lo que no podemos hacer lo siguiente, ya que daría un error. 
# De hecho el error sería TypeError: int' object is not iterable.

# DATOS DE ENTRADA:

# number = 10
# for i in number:
# print(i)

# DATOS DE SALIDA:

# TypeError: int' object is not iterable.