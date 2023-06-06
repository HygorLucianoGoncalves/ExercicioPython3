import moeda

valor = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor)}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,True)}")
print(f"O aumento de 10% e de {moeda.aumentar(valor,10,True)}")
print(f"O desconto de 10% e de {moeda.diminuir(valor,10,True)}")
