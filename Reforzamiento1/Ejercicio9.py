"""9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla."""

num1 = 2
potencia= num1 ** 4 #Tambien puedo usar pow, pero meh :) import math -> math.pow(num1,4)
print(potencia - (potencia*2))