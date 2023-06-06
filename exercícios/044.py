preço = int(input("Preço das compras: R$"))
print(
  "Formas de pagamento\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão"
)
opção = int(input("Qual é a opção? "))

if opção == 1:
  print(
    f"Sua Compra de {preço:.2f} vai custar à vista: R${preço - (preço*10/100):.2f} "
  )
elif opção == 2:
  print(
    f"Sua Compra de {preço:.2f} vai custar à vista no cartão: R${preço - (preço*5/100):.2f}"
  )
elif opção == 3:
  print(
    f"Sua Compra de {preço:.2f} vai custar No cartão 2x: duas pacelas de R${preço / 2:.2f} "
  )
elif opção == 4:
  print(f"Sua compra no valor {preço}")
  parcelas=int(input("qual a pacela? "))
  print(
    f"Sua compras será parcelada em {parcelas}x de R${preço / parcelas:.2f}\nCOM JUROS\nSua compra de R${preço:.2f} vai custar {preço + (preço*20/100):.2f} no final"
  )
else: 
  print("Opção inválida!! Tente novamente...")