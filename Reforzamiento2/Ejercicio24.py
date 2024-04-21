"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""
empleado = {
    "nombre": "Juan",
    "edad": 19,
    "salario": 2234.50,
    "posicion": "Tester"
}
lista1=list(empleado.items())
for i in range(len(lista1)):
    print(type(lista1[i]))