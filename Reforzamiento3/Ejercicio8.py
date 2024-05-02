"""Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios."""

class Persona:
    def __init__(self):
        self.nombre = self.getNombre()
        self.apellido = self.getApellido()
        self.edad = self.getEdad()
    def getNombre(self):
        nombre = input("Ingresa tu nombre: ")
        return nombre
    def getApellido(self):
        apellido = input("Ingresa tu apellido: ")
        return apellido
    def getEdad(self):
        age = int(input("Enter your age: "))
        return age
    def toString(self):
        print(f"Nombre Completo: {self.nombre} {self.apellido} \nEdad: {self.edad}")

persona = Persona()
persona.toString()