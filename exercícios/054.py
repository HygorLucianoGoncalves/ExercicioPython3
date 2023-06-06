import datetime

anoAtual = datetime.date.today().year
contagemmaior = 0
contagem = 0
for i in range(1, 8):
  pessoa = int(input(f"Em que ano a {i}° pessoa nasceu? "))
  if (anoAtual - pessoa) >= 18:
    contagemmaior += 1
  else:
    contagem += 1

print(
  f"\nAo todo tivemos {contagemmaior} pessoas maiores de idade\nE também tivemos {contagem} menores de idade"
)
