import random

numeros = []
for i in range(1, 61):
  numeros.append(i)
print("-" * 30)
print(f"{' '*5} JOGA NA MEGA SENA")
print("-" * 30)
jogos = int(input("\nQuantos jogos quer que eu sorteie? "))
print(f"{'-'*15}  SORTEANDO {jogos} JOGOS  {'-'*15}")
for i in range(1, jogos + 1):
  print(f"\nJogo {i}: {random.sample(numeros, 6)} ")
print(f"{'-'*15}  BOA SORTE  {'-'*15}")

##ou
# import random
# for x in range(int(input('Number of games: '))):
#     print(f'Game {x+1}: {random.sample(range(1, 61), 6)}')
