import moeda

valor = float(input("Digite o preço: R$"))
print(f"A metade de {valor:.2f} é {moeda.metade(valor):.2f}")
print(f"O dobro de {valor:.2f} é {moeda.dobro(valor):.2f}")
print(f"O aumento de 10% e de {moeda.aumentar(valor,10):.2f}")
print(f"O desconto de 10% e de {moeda.diminuir(valor,10):.2f}")
