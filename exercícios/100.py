import random
import time


def sorterio():
  global sort  #variavel global
  numeros = list()
  for i in range(1, 10):
    numeros.append(i)
  sort = random.sample(numeros, 5)
  return sort


n = sorterio()


def pares(valor):
  print("Sorteando 5 valores da lista:", end=" ")
  for i in valor:
    print(i, end=" ", flush=True)
    time.sleep(0.3)
  print('PRONTO!')
  soma = 0
  for i in valor:
    if i % 2 == 0:
      soma += i
  print(f"Somando os valores pares de {sort}, temos {soma}.")


pares(n)
