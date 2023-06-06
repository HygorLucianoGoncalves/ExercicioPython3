teste = list()
teste.append("gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

####

teste = [["gustavo", 19],["maria", 10],["ana", 19],["carol", 20],["olocas", 25]]

print(teste[2][1])

for i in teste:
  print(f"{i[0]} tem {i[1]} ano de idade")


####


galera = list()
dados = list()
totmai = totomen = 0
for c in range(0, 3):
  dados.append(str(input("Nome: ")))
  dados.append(int(input("Idade: ")))
  galera.append(dados[:])
  dados.clear()

print(galera)

for i in galera:
  if i[1] >= 21:
    print(f"{i[0]} é maior de idade.")
    totmai += 1
  else:
    print(f"{i[0]} é  menor de idade")
    totomen += 1
print(f"o total de maior de idade foi {totmai} e os menor foi {totomen}")