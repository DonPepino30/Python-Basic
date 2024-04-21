"""4.Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe
estar en una variable distinta y tú las tienes que asignar. Mostrar el volumen por
pantalla. V = 4/3 π r3"""
import math

radio = input("Porfavor ingrese el radio: ")
volumen = (4/3)* math.pi * (float(radio) **3)
print(volumen)