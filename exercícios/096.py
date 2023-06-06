def area(largura, comprimento):
  area = largura * comprimento
  print(f"A área de um terreno {l}x{c} é de {area}m².")


print('_-' * 15)
print("    Controle de Terrenos")
print('_-' * 15)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)
