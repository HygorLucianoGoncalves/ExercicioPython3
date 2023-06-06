import datetime

data = int(input("Qual sua data de nacimento? "))
anoAtual = datetime.date.today().year
idade = anoAtual - data
print(f"Quem nasceu em {data} tem {idade} anos em {anoAtual}")
if idade < 18:
  print(
    f"Ainda não pode se alista\nFalta {18 - idade} anos para ser alista\nO ano de alitamento sera em {anoAtual +(18 - idade)}"
  )
elif idade > 18:
  print(f"Ja passou do ano de se alista, ja se passou {idade - 18} anos.")
else:
  print("Esta na hora de ser apresentar no quartel nas proximo ")
