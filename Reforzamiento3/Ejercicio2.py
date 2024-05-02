"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

def cuadrados(a, b):
    Li = min(a, b)
    Ls = max(a, b)
    for num in range(Li, Ls + 1):
        cuadradoNum = num ** 2
        print(cuadradoNum)

num1,num2 = int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: "))
cuadrados(num1, num2)