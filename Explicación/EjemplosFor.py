# EJEMPLOS "for":

# Iterando cadena al revés. Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.

# DATOS DE ENTRADA:

text = "Python"

for i in text[::-1]:
    print(i)

# DATOS DE SALIDA:

# n
# o
# h
# t
# y
# P

# Itera la cadena saltándose elementos. Con [::2] vamos tomando un elemento si y otro no.

# DATOS DE ENTRADA:

for i in text[::2]:
    print(i)

# DATOS DE SALIDA:

# P
# t
# o

# Un ejemplo de for usado con comprehensions lists:

# DATOS DE ENTRADA:

print(sum(i for i in range(10)))

# DATOS DE SALIDA:

# 45

# Tiene bastante sentido, porque si queremos iterar una variable, esta variable debe ser iterable, todo muy lógico. 
# Pero llegados a este punto, tal vez de preguntes ¿pero cómo se yo si algo es iterable o no?. 
# Bien fácil, con la siguiente función isinstance() podemos saberlo. 
# No te preocupes si no entiendes muy bien lo que estamos haciendo, fíjate solo en el resultado, True significa que es iterable y False que no lo es.

from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))
print(isinstance(cadena, Iterable))
print(isinstance(numero, Iterable))