print(f"{'='*30}\n        BANCO DESDEV \n{'='*30}")
n1 = n10 = n20 = n50 = 0

valor = int(input("Valor para sacar? R$"))

n50 = int(valor / 50)
valor = valor % 50

n20 = int(valor / 20)
valor = valor % 20

n10 = int(valor / 10)
valor = valor % 10

n1 = valor

if n50 != 0:
  print(f"total de {n50} cédulas de R$50")
if n20 != 0:
  print(f"total de {n20} cédulas de R$20")
if n10 != 0:
  print(f"total de {n10} cédulas de R$10")
if n1 != 0:
  print(f"total de {n1} cédulas de R$1")

#feita na aula
valor = int(input("Valor para sacar? R$"))
total = valor
ced = 50
totalced = 0

while True:
  if total >= ced:
    total -= ced
    totalced += 1
  else:
    if totalced > 0:
      print(f"Total de {totalced} céculas de R${ced}")
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalced = 0
    if total == 0:
      break
