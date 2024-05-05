"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:"""

def diccionarioError(persona, clave):
    try:
        return persona[clave]
    except KeyError as e:
        print(f"Error: La clave {e} no existe en el diccionario")

persona = {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
diccionarioError(persona, 'profesion')

input("Ingrese un valor para comprobar la continuidad del codigo: ")