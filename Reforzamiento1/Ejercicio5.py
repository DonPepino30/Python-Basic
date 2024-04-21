"""5.Crear un programa que, partiendo de un sueldo en una variable, sepamos si es par
o impar. Utilizar módulo y condicional."""

sueldo=input("Ingrese el sueldo: ")

while True:
    if (float(sueldo) % 2 == 0 & float(sueldo) > 0):
        print("sueldo par")
        break
    elif (float(sueldo)>0):
        print("sueldo impar")
        break
    else: print("el sueldo es igual a 0")
    break
