# "for" ANIDADOS:

# Es posible anidar los for, es decir, meter uno dentro de otro. 
# Esto puede ser muy útil si queremos iterar algún objeto que en cada elemento, tiene a su vez otra clase iterable. 
# Podemos tener por ejemplo, una lista de listas, una especie de matriz.

# DATOS DE ENTRADA:

list = [[56, 34, 1],
        [12, 4, 5],
        [9, 4, 3]]

# Si iteramos usando sólo un for, estaremos realmente accediendo a la segunda lista, pero no a los elementos individuales.

for i in list:
    print(i)

# DATOS DE SALIDA:

# [56, 34, 1]
# [12, 4, 5]
# [9, 4, 3]

# Si queremos acceder a cada elemento individualmente, podemos anidar dos for. 
# Uno de ellos se encargará de iterar las columnas y el otro las filas.

# DATOS DE ENTRADA:

for i in list:
    for j in i:
        print(j)

# DATOS DE SALIDA:

# 56
# 34
# 1
# 12
# 4
# 5
# 9
# 4
# 3

