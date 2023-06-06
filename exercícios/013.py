salario = float(input("Qual e o valor do salario do funcionário? R$"))

desconto = salario + (salario*15/100)

print(f"O funcionario que ganhava R${salario:.2f}, com o desconto de 15% de aumento, passa a receber {desconto:.2f} ")