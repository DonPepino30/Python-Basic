"""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

def sumaDeDigitos(n):
    return sum(int(digito) for digito in str(n))
def main():
    num1, num2 = int(input("Ingrese un numero positivo: ")), int(input("Ingrese otro numero positivo: "))
    if num1 <= 0 or num2 <= 0:
        print("ERROR! Ingrese numeros positivos")
        return 0
    sum1 = sumaDeDigitos(num1)
    sum2 = sumaDeDigitos(num2)
    if sum1 > sum2:
        print(f"La suma de digitos de {num1} es mayor.")
    elif sum2 > sum1:
        print(f"La suma de digitos de {num2} es mayor.")
    else:
        print(f"Ambos tienen la misma suma de digitos.")
    if sum1 < 10:
        print(f"{num1} tiene una sumatoria menor a 10.")
    if sum2 < 10:
        print(f"{num2} tiene una sumatoria menor a 10")
if __name__ == "__main__":
    main()