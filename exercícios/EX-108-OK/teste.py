import moeda

valor = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
print(f"O aumento de 10% e de {moeda.moeda(moeda.aumentar(valor,10))}")
print(f"O desconto de 10% e de {moeda.moeda(moeda.diminuir(valor,10))}")
