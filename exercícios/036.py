valorDaCasa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o seu salario: R$"))
anos = int(input("Quantos anos você que pagar: "))

prestação = valorDaCasa / (anos * 12)
print(
  f"Para pegar uma casa de R${valorDaCasa:.2f} em {anos} anos a prestação será de R${prestação:.2f}"
)
if prestação > (salario * 30 / 100):
  print("NEGADO")
else:
  print("APROVADO")
