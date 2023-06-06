primriroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primriroTermo
valor = 10
cont = 0

while cont <= valor:  #engando não chega a 10 continua fazendo o while
  if cont == valor:
    nv = int(input("\nQuantos temos você quer mostrar a mais? "))
    valor += nv
    if nv == 0:
      break
  print(f"{termo} ", end="-> ")
  termo += razao  # termo + razao
  cont += 1
print(f"\nProgressão finalizada com {cont} Termos mostrados")

#  FEITO NA AULA

print("Gerador de PA")
print("-=" * 20)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
  total = total + mais
  while cont <= total:
    print(f"{termo} ->")
    termo += razão
    cont += 1
  print("pausa")
  mais = int(input("Quantos termos voce quer mostrar a mais? "))
print(f"progressão finalizada com {cont} Termos mostrados")
