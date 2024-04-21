"""Crea una nueva lista vacía y agregue ítems (diferentes tipos de datos de manera
desordenada: 3 floats, 3 ints y 3 strings) (append)."""
import random
lista2=[]
lista2.append(10.1)
lista2.append(2.7)
lista2.append(7.6)
lista2.append(12)
lista2.append(5412)
lista2.append(3454)
lista2.append("Soy")
lista2.append("Cadena")
lista2.append("Desordenada")
random.shuffle(lista2)
print(lista2)