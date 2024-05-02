"""Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

def getName():
    nombre = input("Ingresa tu nombre: ")
    return nombre
def getSeguro():
    tipoSeguro = input("Ingresa el tipo de seguro (Autos, Camiones, or Motos): ")
    return tipoSeguro
def verificarEdad():
    edad = int(input("Ingresa tu edad: "))
    return "Mayor de edad" if edad>=18 else "Menor de edad"