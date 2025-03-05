# **_Bucle_For_**

**_A continuación explicaremos el bucle ```for``` y sus particularidades en Python, que comparado con otros lenguajes de comparación, tiene ciertas diferencias._**

- **_El ```for``` es un tipo de bucle, parecido al ```while``` pero con ciertas diferencias._**
  
- **_La principal es que el número de iteraciones de un ```for``` esta definido de antemano, mientras que en un ```while``` no._**
  
- **_La diferencia principal con respecto al ```while``` es en la condición._**
  
- **_Mientras que en el ```while``` la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el ```for``` no existe tal condición, sino un iterable que define las veces que se ejecutará el código._**
  
- **_En el siguiente ejemplo vemos un bucle ```for``` que se ejecuta 5 veces, y donde la ```i``` incrementa su valor “automáticamente” en 1 en cada iteración:_**

```
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
```

- **_Si has leído el capítulo del ```while```, tal vez ya empieces a ver ventajas en el uso del ```for```._**
  
- **_Si por ejemplo, queremos tener un número que va creciendo de ```0``` a ```n```, hacerlo con ```for``` nos ahorra alguna línea de código, porque no tenemos que escribir código para incrementar el número._**

- **_En Python se puede iterar prácticamente todo, como por ejemplo una cadena. En el siguiente ejemplo vemos como la variable ```i``` va tomando los valores de cada letra._**

```
for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n
```

### **_Iterables e iteradores_**

- **_Para entender al cien por cien los bucles ```for```, y como Python fue diseñado como lenguaje de programación, es muy importante entender los conceptos de iterables e iteradores._**

- **_Empecemos con un par de definiciones:_**

- **_Los iterables son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. Si piensas en un array (o una ```list``` en Python), podemos indexarlo con ```lista[1]``` por ejemplo, por lo que sería un iterable._**
  
- **_Los iteradores son objetos que hacen referencia a un elemento, y que tienen un método ```next``` que permite hacer referencia al siguiente._**

- Ambos son conceptos un tanto abstractos y que pueden ser complicados de entender.
- Veamos unos ejemplos. Como hemos comentado, los iterables son objetos que pueden ser iterados o accedidos con un índice. Algunos ejemplos de iterables en Python son las listas, tuplas, cadenas o diccionarios. Sabiendo esto, lo primero que tenemos que tener claro es que en un for, lo que va después del in deberá ser siempre un iterable.
