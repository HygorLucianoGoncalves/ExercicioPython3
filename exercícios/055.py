max = 0
min = 0

for i in range(1, 6):
  peso = float(input(f"Digite o peso da {i}° pessoa: "))
  if i == 1:
    max = peso
    min = peso
  else:
    if peso > max:
      max = peso
    if peso < min:
      min = peso

print(f"O valor lido foi {max}\nE o menor peso lido foi {min}")
