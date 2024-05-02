"""Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""

class Agenda:
    def __init__(self):
        self.contactos = []
    def agregarContactos(self, nombre, fono, mail, dni):
        self.contactos.append({"nombre": nombre, "fono": fono, "mail": mail, "dni": dni})
    def toString(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto['nombre']}")
            print(f"Fono: {contacto['fono']}")
            print(f"mail: {contacto['mail']}")
            print(f"DNI: {contacto['dni']}")
            print()
    def buscarContacto(self, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                print("Contacto encontrado: \n")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Fono: {contacto['fono']}")
                print(f"mail: {contacto['mail']}")
                print(f"DNI: {contacto['dni']}")
                return
        print("\nContacto no encontrado")

agenda = Agenda()
agenda.agregarContactos("Benito Camela", "951378217", "BenitosecZ@gmail.com", "70844995")
agenda.agregarContactos("Zacarias Flores Del Campo", "981231267", "ZacariasBadBoy69@gmail.com", "60129312")
agenda.toString()
agenda.buscarContacto("70844995")
agenda.buscarContacto("99991232")