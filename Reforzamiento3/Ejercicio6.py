"""Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

class Convertidor:
    def __init__(self):
        self.resultado = 0
    def cubo(self, num):
        self.resultado = num ** 3
        return self.resultado
    def cuadrado(self):
        return self.resultado ** 2
    def getNumber(self):
        num = int(input("Ingrese un numero: "))
        return num

ConvertidorCubCuad = Convertidor()
num = ConvertidorCubCuad.getNumber()
ConvertidorCubCuad.cubo(num)
print(f"El cubo de  {num} es: {ConvertidorCubCuad.resultado}")
print(f"El cuadrado del cubo de {num} es: {ConvertidorCubCuad.cuadrado()}")
