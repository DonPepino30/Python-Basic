"""Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario ya creado.
➢ Mostrar en consola los valores de su variable final (ya sea diccionario o lista)."""
departamento_capital={
    "Arequipa":"Chachapoyas",
    "Ancash":"Huaraz",
    "Apurimac":"Abancay",
    "Ica":"Ica",
    "La Libertad":"Trujillo",
    "Loreto":"Iquitos"
}
for departamento, capital in departamento_capital.items():
    carrera = input(f"Ingrese el nombre de la carrera para el departamento '{departamento}' con capital en '{capital}': ")
    departamento_capital[departamento] = (capital, carrera)
print(departamento_capital)