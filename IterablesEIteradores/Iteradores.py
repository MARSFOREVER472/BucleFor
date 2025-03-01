# Una vez entendidos los iterables, veamos los iteradores. 
# Para entender los iteradores, es importante conocer la función iter() en Python. 
# Dicha función puede ser llamada sobre un objeto que sea iterable, y nos devolverá un iterador como se ve en el siguiente ejemplo:

# DATOS DE ENTRADA:

list = [5, 6, 3, 2]
it = iter(list)

print(it) # FORMA 1

print(type(it)) # FORMA 2

# DATOS DE SALIDA:

# <list_iterator object at 0x000001D50F58ABF0>
# <class 'list_iterator'>