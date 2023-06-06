import time

velocidade = int(input("Qual é a sua velocidae atual do carro? "))
print("PROCESSANDO...")
time.sleep(2)
print("-=-" * 20)
if velocidade <= 80:
  print(
    "Velociadade da via e de 80km\nTenha um bom dia! Dirija com segurança!")
else:
  multa = (velocidade - 80) * 7
  print(f"Você foi multado, o valor e R${multa:.2f}  ")
  print("-=-" * 20)
  print(
    "!!!! CUIDADO, esta acima da velocidade permitido na via de 80km/h\nDeve reduzir para que não ocorra acidentes!!!!!!!"
  )
