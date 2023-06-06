medias = {}
medias["nome"] = str(input("Nome do aluno: "))
medias["média"] = float(input("Média do aluno: "))
if medias["média"] < 5.0:
  medias["situação"] = "Reprovado"
elif 5.0 <= medias["média"] < 7.0:
  medias["situação"] = "Recuperação"
else:
  medias["situação"] = "Aprovado"
print("=-"*30)
print(f"   -nome é igual a {medias['nome']}")
print(f"   -média é igual a {medias['média']}")
print(f"   -situação é igual a {medias['situação']}")
# ou 
print("=-"*30)

for k, v in medias.items():
  print(f"   -{k} é igual a {v}")