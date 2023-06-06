#minha resolução

print(f"{'-'*20}\nCADASTRE UMA PESSOA\n{'-'*20}")
maiorIdade = homen = mulher = menorDeVinte = 0

while True:
  idade = int(input("Idade: "))
  sexo = str(input("Sexo: [M/F] ")).strip()[0]
  if idade >= 18:
    maiorIdade += 1
  if sexo in "Mm":
    homen += 1
  if sexo in "Ff":
    mulher += 1
    if idade < 20:
      menorDeVinte += 1
  cont = str(input("Quer continuar? [S/N] ")).strip()[0]
  print("--" * 10)
  if cont in "Nn":
    break
  elif cont in "Ss":
    continue
  else:
    print("Valor ERRADO... Tente novamente")
    print("--" * 10)
print(
  f"Total de pessoas com mais de 18 anos: {maiorIdade}\nAo todo temos {homen} homens cadastrados\nE temos {menorDeVinte} mulheres com menos de 20 anos"
)

#resolução feita no video
tot18 = totH = totM20 = 0
while True:
  idade = int(input("Idade: "))
  sexo = " "
  while sexo not in "MmFf":
    sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
  if idade >= 18:
    tot18 += 1
  if sexo == "M":
    totH += 1
  if sexo == "F" and idade < 20:
    totM20 += 1
  resp = " "
  while resp not in "SN":
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
  if resp == "N":
    break
print(f"Total de pessoas com mais de 18 anos: {tot18} ")
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")
