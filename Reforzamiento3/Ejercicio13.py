"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo) (si sueldo es superior a 4000 soles)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    def toStringSalario(self):
        if self.salario > 4000:
            impuesto = self.salario * 0.1
            print(f"Salario: {self.salario}")
            print(f"Impuesto: {impuesto}")
        else:
            print(f"Salario: {self.salario}")
            print("No hay impuestos")

e1 = Empleado("Benito Camela", 28, 8000)
e1.toStringSalario()