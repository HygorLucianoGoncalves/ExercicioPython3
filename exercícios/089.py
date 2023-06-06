ficha = list()
while True:
  nome = str(input("nome :"))
  nota1 = float(input("Nota1: "))
  nota2 = float(input("Nota2: "))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input("Quer contunuar? [S/N]: "))
  if resp in "Nn":
    break
print("=" * 30)
print(f"{'NO.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("=" * 30)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  print("-" * 15)
  opc = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
  if opc == 999:
    break
  if opc <= len(ficha) - 1:
    print(f"notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("FIMMMMMMM")


############################

dados = list()
while True:
  nome = (str(input("Nome: ")))
  nota1 = (float(input("Nota 1: ")))
  nota2 = (float(input("Nota 2: ")))
  media = (nota1 + nota2) / 2
  dados.append([nome, nota1, nota2, media])
  r = " "
  while r not in "SsNn":
    print("-" * 30)
    r = str(input("Quer continuar? [S/N]")).strip()
  if r in "Nn":
    break
print("=" * 30)
print(f"{'NO.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("=" * 30)
for i, a in enumerate(dados):
   print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  print("-" * 15)
  opc = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
  if opc == 999:
    break
  if opc <= len(dados) - 1:
    print(f"notas de {dados[opc][0]} são {dados[opc][1]}")
print("FIMMMMMMM")
