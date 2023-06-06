import math

valor = int(input("Digite o valor do angulo: "))
valor1 = math.radians(valor)

cosa = math.cos(valor1)
sen0 = math.sin(valor1)
tann = math.tan(valor1)

print(
  f"o valor da cosseno e {cosa:.2f}\nO valor do seno e {sen0:.2f}\nO valor da tangente e {tann:.2f}"
)
