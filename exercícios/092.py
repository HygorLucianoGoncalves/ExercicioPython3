import datetime

info = dict()
dataAtual = datetime.date.today().year
info["nome"] = str(input("Nome: "))
info["naci"] = int(input("Ano de nascimento: "))
info["ct"] = int(input("Carteira de trabalho (0 não tem): "))
if info["ct"] != 0:
  info["anoContra"] = int(input("Ano da Contratção: "))
  info["salario"] = int(input("Salário tem o valor R$: "))
print("-="*30)
print()
idade = dataAtual - info['naci'] 
print(f"    -{info['nome']} tem as seguintes informação ")
print(f"    -Idade de {info['nome']} e de {idade} anos")
print("    -Não tem Carteira de trabalho")
if info['ct'] != 0:
  print(f"    -ctps tem o valor {info['ct']}")
  print(f"    -Contratação tem valor de {info['anoContra']} ")
  print(f"    -Salário tem o valor {info['salario']:2f}R$")
  apos = (info['anoContra'] + 70) - dataAtual
  print(f"    -Se Aposentadoria com {apos} anos")
