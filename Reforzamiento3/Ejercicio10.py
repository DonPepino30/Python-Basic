"""Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""

class Persona:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    def toString(self):
        if self.edad >= 18:
            condicion = "Mayor de edad"
        else:
            condicion = "Menor de edad"
        print(f"Nombre Completo: {self.nombre}")
        print(f"Edad: {self.edad} ({condicion})")
        print(f"Salario: {self.salario}")
        print(f"Bono: {self.Bono()}")
    def Bono(self):
        return self.salario * 0.2

p1 = Persona("Juan Perez", 20, 3000)
p2 = Persona("Zacarias Flores Del Campo", 11, 500)
p1.toString()
p2.toString()
