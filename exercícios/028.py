import random
import time

Usuario = str(input(
  "Bem Vindo ao jogo de advinhação.\nQual seu nick: ")).strip().capitalize()
print("-" * 20)
print(f"Ola {Usuario}, vou pensar em um número entre 0 e 5. tente adivinha...")
print("-" * 20)
nu = int(input("Qual numero estou pensando: "))
sorteio = random.randint(0, 5)
print("PROCESSANDO...")
time.sleep(2)
print("-" * 20)
if nu == sorteio:
  print(f"Parabens {Usuario} você acertou!!!")
else:
  print(
    f"{Usuario} você foi de americanas, tente novamente.\n\n                    O numero foi {sorteio}"
  )