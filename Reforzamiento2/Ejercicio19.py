"""Crea una lista vacía que tendrá 10 valores enteros, pedir al usuario que ingrese cada
uno de sus valores y que finalmente se muestre la suma y la media de los números
ingresados a la lista."""
suma = 0
lista1=[]
for i in range(10):
    lista1.append(int(input("Ingrese un entero: ")))
    suma+=lista1[i]
print(suma/ len(lista1))