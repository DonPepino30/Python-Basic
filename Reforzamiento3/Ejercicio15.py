"""Crea un módulo llamado generador.py que cumpla los siguientes requisitos:
• Tendrá una función llamada leer_numero(). Esta función tomará 2
valores: ini y fin, ingresado por consola. Que serán los límites de los
números a crear.
• Una vez la tengas los números, deberás crear una nueva función
llamada generador, no recibirá ningún parámetro. Dentro usarás la
función leer_numero():
• En la cual se creará una lista donde los números que tendrá
esta lista serán los números obtenidos en la primera
función (respetando el ini y fin)
• Esta función devolverá el cuadrado de todos esto números
que están dentro de la lista.

• Finalmente importando estas funciones respectivamente en el archivo
main.py (principal) se mostrarán los números cuadrados"""

import generador

ini = int(input("Ingrese el limite inferior: "))
fin = int(input("Ingrese el limite superior: "))
listaCuadrados = generador.generador(ini, fin)
print("Cuadrados:")
for cuadrado in listaCuadrados:
    print(cuadrado)