lista = list()
cont = 0

while True:
  lista.append(int(input("Digite um valor: ")))
  cont += 1
  r = " "
  while r not in "SN":
    r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if r == "N":
    break
  print('-' * 30)
d = sorted(lista, key=int, reverse=True)
print('-' * 30)
print(f"Voce digitou {cont} elementos.")  #ou no lugar do cont coloca len()
print(f"Os valores em ordem decrescente são {d}")
if 5 not in lista:
  print("o valor 5 não foi encotrado na lista")
else:
  print("o valor 5 foi encotrado na lista")

# #r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
#   if r in "N":
#     break
