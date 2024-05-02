"""Crear una clase llamada círculo que contenga radio en su constructory
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

import math

class Circulo:
    def __init__(self, radio):
        try:
            self.radio = float(radio)
        except ValueError:
            raise ValueError("Error! El radio debe ser un numero")
    def area(self):
        return math.pi * (self.radio ** 2)
    def perimetro(self):
        return 2 * math.pi * self.radio
    def getRadio(self):
        radio = input("Ingrese el radio: ")
        self.radio = float(radio)

def main():
    try:
        c2 = Circulo("hola")
        c2.getRadio()
    except ValueError as e:
        print(e)

    c1 = Circulo(5)
    c1.getRadio()
    print(f"Area del circulo 1: {c1.area()}")
    print(f"Perimetro del circulo 1: {c1.perimetro()}")

if __name__ == "__main__":
    main()