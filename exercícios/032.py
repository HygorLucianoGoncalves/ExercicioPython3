import calendar
import datetime

ano = int(input("Digite o ano, Coloque 0 para analisar o ano atual:  "))
if ano == 0:
  ano = datetime.date.today().year

bis = calendar.isleap(ano)

if bis == True:
  print(f"{ano} esse ano e Bissexto")
else:
  print(f"{ano} esse ano não e Bissexto")
