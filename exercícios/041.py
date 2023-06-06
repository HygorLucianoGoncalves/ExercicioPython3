import datetime

ano = int(input("Ano de Nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual - ano

print(
  f"O Atleta naceu no ano de {ano} e tem {idade} anos em {anoAtual} Sua classificação e: "
)

if idade < 9:
  print("Atleta MIRIM")
elif idade <= 14:
  print("Atleta INFANTIL")
elif idade <= 19:
  print("Atleta JUNIOR")
elif idade <= 25:
  print("Atleta SENIOR")
else:
  print("Atleta MASTER")