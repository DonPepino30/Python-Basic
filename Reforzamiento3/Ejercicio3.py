"""Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos."""
def sumaDeDigitos(n):
    return sum(int(digito) for digito in str(n))

num = int(input("Ingrese un numero: "))
print(f"La suma de digitos es: {sumaDeDigitos(num)}")
