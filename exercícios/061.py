primriroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primriroTermo
cont = 1
while cont <= 10:  #engando não chega a 10 continua fazendo o while
  print(f"{termo}", end=" ")
  termo += razao  # termo + razao
  cont += 1
print("FIM")