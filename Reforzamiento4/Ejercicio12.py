"""12. Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”."""

def saludo(fun):
    def saludoInterno():
        print("Buenos días!")
        nombre = input("Cuál es tu nombre? ")
        resultado = fun(nombre)
        print("Hasta luego!")
        return resultado

    return saludoInterno

@saludo
def saludarPersona(nombre):
    return f"Soy {nombre}"

print(saludarPersona())
