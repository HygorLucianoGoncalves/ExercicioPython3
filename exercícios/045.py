import random  
import time

user = str(input("Ola Qual seu nome? : ")).strip().capitalize()
print("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")

opção = int(input(f"Qual e sua jogada {user}? "))

list = ("PEDRA", "PAPEL", "TESOURA")
sorteio = random.choice(list)

print("-=-"*10)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ")
print("-=-"*10)

if opção == 0:
  print(f"O computador jogou {sorteio}\nO Jogador: {user} jogou PEDRA")
  if sorteio == "PEDRA":
    print("EMPATE")
  elif sorteio == "PAPEL":
    print("Jogador PERDEU")
  else:
    print("Jogador GANHOU")
elif opção == 1:
  print(f"O computador jogou {sorteio}\nO jogador: {user} jogou PAPEL")
  if sorteio == "PEDRA":
    print("Jogador GANHOU")
  elif sorteio == "PAPEL":
    print("EMPATE")
  else:
    print("Jogador PERDEU")
elif opção == 2:
  print(f"O computador jogou {sorteio}\nO Jogador: {user} jogou TESOURA")
  if sorteio == "TESOURA":
    print("EMPATE")
  elif sorteio == "PAPEL":
    print("Jogador GANHOU")
  else:
    print("Jogador PERDEU")
else:
  print("Opção inválida!! Tente novamente...")