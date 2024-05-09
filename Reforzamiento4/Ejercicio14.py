"""14. Crear un decorador donde imprimirá la cantidad de argumentos que
tiene la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”"""

def contadorArgs(func):
    def funcA(*args, **kwargs):
        print(f"La cantidad de argumentos que tiene la función es {len(args) + len(kwargs)}")
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente.")
        return resultado
    return funcA

@contadorArgs
def multiplicar(a, b, c, d):
    return a * b * c * d
print(multiplicar(2, 3, 5, 8))
