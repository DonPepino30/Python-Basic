"""Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)"""

class Estudiante:
    def __init__(self, nombre, edad, notaFinal):
        self.nombre = nombre
        self.edad = edad
        self.notaFinal = notaFinal
    def toString(self):
        notificacion = "Aprobado" if self.notaFinal >= 11 else "Jalado XD"
        print(f"Nombre Completo: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota final: {self.notaFinal}")
        print(f"{notificacion}")

s1 = Estudiante("Juan Perez", 15, 9)
s2 = Estudiante("Zacarias Flores Del Campo", 14, 20)
s3 = Estudiante("Benito Camela", 20, 3)
s1.toString()
s2.toString()
s3.toString()