"""7.De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los
valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la
suma."""

import random

A1 = random.uniform(3,5)
A2 = random.uniform(5,10)
A3 = random.uniform(14,21)

M1 = A1%3
M2 = A2%5
M3 = A3%7

print(M1+M2+M3)