"""11. Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”"""

def guardarDatos(nombre, nota1, nota2):
    with open("calificaciones.txt", "a") as file:
        promedio = (nota1 + nota2) / 2
        file.write(f"{nombre},{nota1},{nota2},{promedio}\n")

def calificar(nombre):
    with open("calificaciones.txt", "r") as file:
        lineas = file.readlines()
        for linea in lineas:
            dato = linea.strip().split(",")
            if dato[0] == nombre:
                promedio = float(dato[3])
                if promedio >= 5:
                    print(f"Alumno {nombre}, aprobado")
                else:
                    print(f"Alumno {nombre}, desaprobado")
                return
        print(f"No se encontró al alumno {nombre}")

guardarDatos("Pedro Pe", 10, 12)
guardarDatos("Mascaly", 4, 5)
calificar("Pedro Pe")
calificar("Mascaly")
calificar("random")