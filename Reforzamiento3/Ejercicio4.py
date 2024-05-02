"""Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada."""

def contarDePalabras(sentence):
    palabras = sentence.split()
    print("La oración contiene:", len(palabras), "palabras.")

oracion = input("Ingrese una oracion de 3 palabras: ")
if len(oracion.split()) == 3:
    contarDePalabras(oracion)
else:
    print("Su oracion no tiene exactamente 3 palabras.")
