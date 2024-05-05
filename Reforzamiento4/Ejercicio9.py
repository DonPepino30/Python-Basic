"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""

def crearTabla(numero):
    if not isinstance(numero, int) or numero < 1 or numero > 20:
        raise ValueError("El número debe ser entero y estar entre 1 y 20.")

    with open("tabla.txt", "w") as f:
        for i in range(1, numero+1):
            f.write(f"{numero} x {i} = {numero * i}\n")

    print("La tabla de multiplicar ha sido guardada en el archivo 'tabla.txt'.")

try:
    numero = int(input("Introduce un número entero entre 1 y 20: "))
    crearTabla(numero)
except ValueError as e:
    print(e)