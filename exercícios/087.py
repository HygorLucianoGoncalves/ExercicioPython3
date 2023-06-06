matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0
for l in range(0, 3):
  for c in range(0, 3):
    n = int(input(f"digite um valor para [{l}, {c}]: "))
    matriz[l][c] = n
    if n % 2 == 0:
      par += n
    if soma >= 0:
      soma += matriz[l][2]
    if maior >= 0:
      matriz[1][c] > maior
      maior = matriz[1][c]
print("-=" * 30)
for l in range(0, 3):
  for c in range(0, 3):
    print(f"[{matriz[l][c]:^5}]", end="")
  print()
print("-=" * 30)
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da terceira coluna é {soma}")
print(f"o maior valor da segunda linha é {maior}")
