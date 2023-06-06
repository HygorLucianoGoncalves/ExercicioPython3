lista = list()
while True:
  n = lista.append(int(input("Digite um valor: ")))
  par = []
  impar = []
  for i in lista:
    if i % 2 == 0:
      par.append(i)
    else:
      impar.append(i)
  r = " "
  while r not in "SsNn":
    r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if r in "Nn":
    break
  print('-' * 30)
print('-' * 30)
print(f"Os valore digitados foram {lista}")
print(f"Os valore PARES são {par}")
print(f"Os valores IMPARES são {impar}")
