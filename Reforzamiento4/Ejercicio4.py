"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:"""


def errorDivision(string):
    try:
        return string / 0
    except TypeError as e:
        print(f"Error: No se puede dividir un string entre un entero {e}")
        return None

errorDivision("Hello Pythonista")
input("Ingrese un valor para comprobar la continuidad del codigo: ")
