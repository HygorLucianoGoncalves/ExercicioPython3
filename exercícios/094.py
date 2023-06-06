dados = dict()
cont = media = soma = 0
nf = []
acm = []
while True:
  dados["nome"] = str(input("Nome: ")).strip().capitalize()
  dados["sexo"] = " "
  while dados["sexo"] not in "MmFf":
    dados["sexo"] = str(input("Sexo? [M/F]: ")).strip().upper()[0]
  dados["idade"] = int(input("Idade: "))
  cont += 1
  soma += dados["idade"]
  media = soma / cont
  if dados["sexo"] in "Ff":
    nf.append(dados["nome"])
  if dados["idade"] > int(media):
    acm.append(dados.copy())
  resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  while resp not in "SN":
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("Erro! Responda apenas S ou N.")
  if resp in "N":
    print("*" * 30)
    break
print(f"A) Ao todo temos {cont} pessoas cadastradas.")
print(f"B) A média de idade é de {media} anos.")
print(f"C) As mulheres cadastradas fora", end=" ")
for i in nf:
  print(f"{i}, ")
print("D) lista das pessoas que estão acima da média:")
for i in acm:
  print(f"    {i}")
print("<<<<<  FIMMMM  >>>>>")
