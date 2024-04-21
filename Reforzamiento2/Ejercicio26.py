"""Crear un diccionario con 6 departamentos en el país. //Creo que esta mal asi que hare departamento-capital
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario."""
departamento_capital={
    "Arequipa":"Chachapoyas",
    "Ancash":"Huaraz",
    "Apurimac":"Abancay",
    "Ica":"Ica",
    "La Libertad":"Trujillo",
    "Loreto":"Iquitos"
}
print(departamento_capital) #Muestra antes de eliminar
del departamento_capital["Ica"]
if "Ica" not in departamento_capital:
    print("El departamento no se encuentra en la biblioteca")