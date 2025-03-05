# Una vez entendidos los iterables, veamos los iteradores. 
# Para entender los iteradores, es importante conocer la función iter() en Python. 
# Dicha función puede ser llamada sobre un objeto que sea iterable, y nos devolverá un iterador como se ve en el siguiente ejemplo:

# DATOS DE ENTRADA:

# list = [5, 6, 3, 2]
# it = iter(list)

# print(it) # FORMA 1

# print(type(it)) # FORMA 2

# DATOS DE SALIDA:

# <list_iterator object at 0x000001D50F58ABF0>
# <class 'list_iterator'>

# Vemos que al imprimir it es un iterador, de la clase list_iterator. 
# Esta variable iteradora, hace referencia a la lista original y nos permite acceder a sus elementos con la función next(). 
# Cada vez que llamamos a next() sobre it, nos devuelve el siguiente elemento de la lista original. 
# Por lo tanto, si queremos acceder al elemento 4, tendremos que llamar 4 veces a next(). 
# Nótese que el iterador empieza apuntando fuera de la lista, y no hace referencia al primer elemento hasta que no se llama a next() por primera vez.

list = [5, 6, 3, 2]
it = iter(list)

print(next(it)) # ITERADOR 1...

#     [5, 6, 3, 2]
#      ^
#      |
#     it

print(next(it)) # ITERADOR 2...

#     [5, 6, 3, 2]
#         ^
#         |
#        it

print(next(it)) # ITERADOR 3...

#     [5, 6, 3, 2]
#            ^
#            |
#           it

print(next(it)) # ITERADOR 4...

#     [5, 6, 3, 2]
#               ^
#               |
#              it

# Existen otros iteradores para diferentes clases:

# - str_iterator para cadenas
# - list_iterator para sets.
# - tuple_iterator para tuplas.
# - set_iterator para sets.
# - dict_keyiterator para diccionarios.

# Dado que el iterador hace referencia a nuestra lista, si llamamos más veces a next() que la longitud de la lista, 
# se nos devolverá un error "StopIteration". 

# Lamentablemente no existe ninguna opción de volver al elemento anterior.

lista = [5, 6] # SE CREA UNA LISTA CON 2 VALORES DENTRO DE UN ARREGLO...
it = iter(lista) # LLAMAREMOS A UN ITERADOR, EN ESTE CASO SERÍA "lista"...

print(next(it)) # SE HACE REFERENCIA AL SIGUIENTE SI HAY UN ELEMENTO DENTRO DE UN ARREGLO, EN CASO DE QUE NO EXISTA, SE DESPLIEGA UN MENSAJE DE ERROR...

#     [5, 6]
#      ^
#      |
#     it

print(next(it))

#     [5, 6]
#         ^
#         |
#        it

# print(next(it))

# StopIteration

# Es perfectamente posible tener diferentes iteradores para la misma lista, y serán totalmente independientes. 
# Tan solo dependerán de la lista, como es evidente, pero no entre ellos.

lista1 = [5, 6, 7]

it1 = iter(lista1) # ITERADOR 1...
it2 = iter(lista1) # ITERADOR 2...

print(next(it1))

#     [5, 6, 7]
#      ^
#      |
#     it

print(next(it1))

#     [5, 6, 7]
#         ^
#         |
#        it

print(next(it1))

#     [5, 6, 7]
#            ^
#            |
#           it

print(next(it2))

#     [5, 6, 7]
#      ^
#      |
#     it

print(next(it2))

#     [5, 6, 7]
#         ^
#         |
#        it

print(next(it2))

#     [5, 6, 7]
#            ^
#            |
#           it