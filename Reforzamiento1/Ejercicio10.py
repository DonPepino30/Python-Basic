"""10. Crear un diccionario con los siguientes key: nombre, carrera, edad y año de
nacimiento, mostrar en pantalla el valor de este diccionario."""

estudiante = {
    "nombre": "Frakaima",
    "carrera": "Ingeniería de Sistemas",
    "edad": 20,
    "año de nacimiento": 2003
}

for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")