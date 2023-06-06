n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print(
  f"Tirando {n1} e {n2}, a média do aluno é {media:.1f}\nO aluno esta em: ")

if media < 5.0:
  print("                REPROVADO")
elif media == 5.0 or media < 6.9:
  print("                RECUPERAÇÃO")
else:
  print("                APROVADA")
