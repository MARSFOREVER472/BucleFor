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