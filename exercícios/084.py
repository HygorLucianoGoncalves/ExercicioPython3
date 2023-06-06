dados = list()
info = list()
cont = 0

while True:
  #colocando os dados nas list
  dados.append(str(input("Nome: ")))
  dados.append(float(input("peso: ")))
  info.append(dados[:])
  dados.clear()

  cont += 1
  #max e min
  for i in info:
    if cont == 1:
      maior = menor = i[1]
    else:
      if i[1] > maior:
        maior = i[1]
      if i[1] < menor:
        menor = i[1]
  #continue ou break
  r = " "
  while r not in "SsNn":
    r = str(input("Você quer continuar? [S/N] "))
  if r in "Nn":
    print("-=" * 20)
    break

print(f"ao todo, você cadastrou {cont} pessoas")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")
#nane in maior
for x in info:
  if x[1] == maior:
    print(f"{x[0]}", end="")
print(f"O menor peso foi de {menor}kg. Pedo de ", end="")
#name in menor
for p in info:
  if p[1] == menor:
    print(f"{x[0]}", end="")
