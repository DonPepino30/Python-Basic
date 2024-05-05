"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:"""

def funcion_con_excepcion():
    try:
        lista = [2, 6, 10, 4, 5, 23, 1]
        print(lista[10])
    except IndexError as e:
        print(f'ERROR!: {e}')

funcion_con_excepcion()
input("Ingrese un dato para comprobar que el codigo no se detuvo: ")