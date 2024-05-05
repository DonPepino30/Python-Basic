"""Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:"""
"""AL FIN UN EJERCICIO BIEN REDACTADO"""

def sumaError():
    try:
        suma = 80 + "Hola Pythonista"
    except TypeError as e:
        print(f"Error!!: {e}")

sumaError()