"""Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último impar).
- Empezando desde 1 y no 0.
- Agregar una cadena en la posición 3 de la lista.
- Eliminar un valor impar de la cadena usando del."""
lista1=[]
num=1

while len(lista1)!=15:
    if num%2!=0:
        lista1.append(num)
    num += 1

for i in range(3):
    num2 = lista1[i]+ 0.10
    lista1.append(num2)

del lista1[4]
lista1.insert(3,"GustaNoHaceSusTareas")
print(lista1)