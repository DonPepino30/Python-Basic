def leerNumeros(ini, fin):
    numeros = []
    for i in range(ini, fin + 1):
        num = int(input(f"Ingrese el numero {i}: "))
        numeros.append(num)
    return numeros

def generador(ini, fin):
    numeros = leerNumeros(ini, fin)
    cuadrados = [num ** 2 for num in numeros]
    return cuadrados