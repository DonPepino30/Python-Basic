"""Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""

class CadenaDePalabras:
    def revertirCadena(self, s):
        return ' '.join(reversed(s.split()))

cadena1 = CadenaDePalabras()
s1 = "Hola Pythonista seguimos adelante"
print(f"Original: {s1}")
print(f"Revertido: {cadena1.revertirCadena(s1)}")