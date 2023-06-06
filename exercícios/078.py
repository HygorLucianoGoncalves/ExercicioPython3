lista = list()
for i in range(0, 5):
  lista.append(int(input(f"Digite um valor para a Posição {i}: ")))
print(f"Você digitou os valores {lista}")
a = max(lista)
b = min(lista)
print(f"\nO maior valor digitado foi {a} nas posição ", end=" ")
for x, v in enumerate(lista):
  if v == a:
    print(f"{x}...", end=" ")

print(f"\nO menor valor digitado foi {b} nas posição ", end=" ")
for x, v in enumerate(lista):
  if v == b:
    print(f"{x}...", end=" ")
