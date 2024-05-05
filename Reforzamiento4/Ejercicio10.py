"""10. Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas."""

def guardarDatos():
    try:
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = int(input("Ingresa tu edad: "))

        with open("agenda.txt", "a") as file:
            file.write(f"{nombre},{apellido},{edad}\n")

    except (ValueError,Exception) as e:
        print(e)

guardarDatos()