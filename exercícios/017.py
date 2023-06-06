import math 

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento de cateto adjacente: "))

h = math.hypot(oposto, adjacente)

print(f"A hipotenusa vai medir {h:.2f}" )