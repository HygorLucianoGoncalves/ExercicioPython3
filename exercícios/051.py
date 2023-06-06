priTer = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = priTer + (10 - 1) * razão
for i in range(priTer, décimo + razão, razão):
  print(f"{i} ", end="-> ")
print("ACABOU")
