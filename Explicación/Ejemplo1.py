# A continuación explicaremos el bucle for y sus particularidades en Python, 
# que comparado con otros lenguajes de comparación, tiene ciertas diferencias.

# El for es un tipo de bucle, parecido al while pero con ciertas diferencias. 
# La principal es que el número de iteraciones de un for esta definido de antemano, mientras que en un while no. 
# La diferencia principal con respecto al while es en la condición. 
# Mientras que en el while la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, 
# en el for no existe tal condición, 
# sino un iterable que define las veces que se ejecutará el código. 
# En el siguiente ejemplo vemos un bucle for que se ejecuta 5 veces, 
# y donde la i incrementa su valor “automáticamente” en 1 en cada iteración.

# DATOS DE ENTRADA:

for i in range(0, 5):
    print(i)

# DATOS DE SALIDA:

# 0
# 1
# 2
# 3
# 4

# Si has leído el capítulo del while, tal vez ya empieces a ver ventajas en el uso del for. 
# Si por ejemplo, queremos tener un número que va creciendo de 0 a n, hacerlo con for nos ahorra alguna línea de código, 
# porque no tenemos que escribir código para incrementar el número.
# En Python se puede iterar prácticamente todo, como por ejemplo una cadena. 
# En el siguiente ejemplo vemos como la i va tomando los valores de cada letra. 
# Mas adelante explicaremos que es esto de los iterables e iteradores.

# DATOS DE ENTRADA:

for i in "Python":
    print(i)

# DATOS DE SALIDA:

# P
# y
# t
# h
# o
# n