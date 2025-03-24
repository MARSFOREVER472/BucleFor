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

- **_Para entender al cien por cien los bucles ```for```, y como Python fue diseñado como un lenguaje de programación, es muy importante entender los conceptos de iterables e iteradores._**

- **_Empecemos con un par de definiciones:_**

- **_Los iterables son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. Si piensas en un array (o una ```list``` en Python), podemos indexarlo con ```lista[1]``` por ejemplo, por lo que sería un iterable._**
  
- **_Los iteradores son objetos que hacen referencia a un elemento, y que tienen un método ```next``` que permite hacer referencia al siguiente._**

- **_Ambos son conceptos un tanto abstractos y que pueden ser complicados de entender._**
  
- **_Veamos unos ejemplos. Como hemos comentado, los iterables son objetos que pueden ser iterados o accedidos con un índice._**
  
- **_Algunos ejemplos de iterables en Python son las listas, tuplas, cadenas o diccionarios._**
  
- **_Dicho esto, lo primero que tenemos que tener claro es que dentro de un ```for```, lo que va después del ```in``` deberá ser siempre un iterable._**

```
#for <variable> in <iterable>:
#    <Código>
```

- **_Tiene bastante sentido, porque si queremos iterar una variable, esta variable debe ser iterable, todo muy lógico._**
  
- **_Pero llegados a este punto, tal vez de preguntes ¿pero cómo se yo si algo es iterable o no?. Bien fácil, con la siguiente función ```isinstance()``` podemos saberlo._**
  
- **_No te preocupes si no entiendes muy bien lo que estamos haciendo, fíjate solo en el resultado, ```True``` significa que es iterable y ```False``` que no lo es._**

``` 
from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False
```

- **_Por lo tanto las listas y las cadenas son iterables, pero la variable ```numero```, que es un entero no lo es._**
  
- **_Es por eso por lo que no podemos hacer lo siguiente, ya que daría un error._**
  
- **_De hecho el error sería ```TypeError: int' object is not iterable```._**

```
numero = 10
#for i in numero:
#    print(i)
```

- **_Una vez entendidos los iterables, veamos los iteradores._**
  
- **_Para entender los iteradores, es importante conocer la función iter() en Python._**
  
- **_Dicha función puede ser llamada sobre un objeto que sea iterable, y nos devolverá un iterador como se ve en el siguiente ejemplo._**

```
lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828>
print(type(it)) #<class 'list_iterator'>
```

- **_Vemos que al imprimir ```it``` es un iterador, de la clase ```list_iterator```._**
  
- **_Esta variable iteradora, hace referencia a la lista original y nos permite acceder a sus elementos con la función ```next()```._**
  
- **_Cada vez que llamamos a ```next()``` sobre ```it```, nos devuelve el siguiente elemento de la lista original. Por lo tanto, si queremos acceder al elemento ```4```, tendremos que llamar 4 veces a next()._**
  
- **_Nótese que el iterador empieza apuntando fuera de la lista, y no hace referencia al primer elemento hasta que no se llama a next() por primera vez._**
