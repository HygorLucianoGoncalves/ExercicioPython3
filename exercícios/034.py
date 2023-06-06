salario = float(input("Informe o valor do salario: R$"))

if salario >= 1250.00:
  print(
    f"Quem ganhava {salario:.2f} passa a ganhar R${salario + (salario*10/100):.2f}"
  )
else:
  print(
    f"Quem ganhava {salario:.2f} passa a ganhar R${salario + (salario*15/100):.2f}"
  )
