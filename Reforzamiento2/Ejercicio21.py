"""Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola."""
empleado = {
    "nombre": "Juan",
    "edad": 19,
    "salario": 2234.50,
    "posicion": "Tester"
}
lista1=list(empleado.items())
print(type(lista1))