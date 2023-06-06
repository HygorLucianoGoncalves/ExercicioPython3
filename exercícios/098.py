def contagem(i, f, p):
  if p < 0:
    p *= -1
  if p == 0:
    p = 1

  print("-_" * 30)
  print(f"Contagem de {i} ate {f} de {p} em {p}")
  if i < f:
    cont = i
    while cont <= f:
      print(f"{cont}", end=" ")
      cont += p
    print("FIM")
  else:
    cont = i
    while cont >= f:
      print(f"{cont}", end=" ")
      cont -= p
    print("FIM")


contagem(1, 10, 1)
contagem(10, 0, 2)
print("-_" * 30)
i = int(input("INICIO: "))
f = int(input("FIM: "))
p = int(input("PASSO: "))
contagem(i, f, p)
