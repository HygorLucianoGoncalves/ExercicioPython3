print(f"{'-'*20} LOJA SUPER BARATÂO {'-'*20}")
total = maiorDe1000 = contagem = menor = nome = 0
while True:
  nomeDoProduto = str(input("Nome do produto: ")).strip()
  preço = float(input("Preço: R$"))
  total += preço
  contagem += 1
  if preço > 1000:
    maiorDe1000 += 1
  if contagem == 1:
    menor = preço
    nome = nomeDoProduto
  else:
    if preço < menor:
      menor = preço
      nome = nomeDoProduto
  cont = " "
  while cont not in "SN":
    cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if cont == "N":
    break

print(f"{'-'*20} FIM DO PROGRAMA {'-'*20}")
print(f"O total da compra foi R${total:.2F}")
print(f"Temos {maiorDe1000} produtos custando mais de R$1000.00")
print(f"O produto mais batato foi {nome} que custa R${menor:.2f}")

