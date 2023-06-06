
#VARIAVEL USADA PARA ICREMETAÇÃO DOS DADOS
somaidade = 0
médiaidade = 0
idadee = 0
maiorIdadeHomen = 0
nomeVelho =""
totmulher20 = 0

for i in range(1, 5):
  # AQUI FAZEMOS A COLETA DAS INFOMAÇÃO 
  print(f"---- {i}° pessoa ----")
  nome = str(input("nome: ")).strip()
  idade = int(input("Idade: "))
  sexo = str(input("sexo [M/F]: ")).strip()
  # AQUI ACONTECE A SOMA DA IDADE DE TODOS
  somaidade += idade
  #A AQUI FAZENDO A PESQUISA DO HOMEM MAIS VELHO DO GRUPO
  if i == 1 and sexo in "Mm":
    maiorIdadeHomen = idade
    nomeVelho = nome
  if sexo in "Mm" and idade > maiorIdadeHomen:
    maiorIdadeHomen = idade
    nomeVelho = nome
    #AQUI PESQUISAMOS AS MULHERES COM MENOS DE VINTE ANOS 
  if sexo in "Ff" and idade < 20:
    totmulher20 +=1        
    #AQUI ACONTECE A CONTA DA MEDIA DE IDADE DO GRUPO DE 4 PESSOAS
médiaidade = somaidade / 4

print(f"\033[49mA media da idade do grupo e {médiaidade}\nO homen mais velho tem {maiorIdadeHomen} anos e se chama {nomeVelho}\nAo todo {totmulher20} mulheres com menos de 20 anos ")









somaIdade = 0
mediaIdade = 0
homenVelho = 0
nameOld = ""
mulheres = 0
ageMulher = 0
for c in range(1, 5):
  print(f"----- {c}° pessoa -----")
  name = str(input("Nome: ")).strip().capitalize()
  age = int(input("Idade: "))
  sex = str(input("Sexo [M/F]: ")).strip().upper()
  somaIdade += age
  if sex == "M":
    if c == 1:
      homenVelho = age
      nameOld = name
    else:
      if age > homenVelho:
        homenVelho = age
        nameOld = name
  if sex == "F" and age < 20:
    ageMulher += 1
    if sex == "F":
      mulheres += 1
mediaIdade = somaIdade / 4
print(f"A medía de idade do grupo é de {mediaIdade} anos")
print(f"O homen mais velho tem {homenVelho} anos e se chama {nameOld}")
print(f"Ao todos são {mulheres} mulheres ao todo e {ageMulher} mulheres são menos de 20 anos")




#com cor no terminal

somaIdade = 0
mediaIdade = 0
homenVelho = 0
nameOld = ""
mulheres = 0
ageMulher = 0
for c in range(1, 5):
  print(f"\033[1m----- {c}° pessoa -----")
  name = str(input("Nome: ")).strip().capitalize()
  age = int(input("Idade: "))
  sex = str(input("Sexo [M/F]: ")).strip().upper()
  somaIdade += age
  if sex == "M":
    if c == 1:
      homenVelho = age
      nameOld = name
    else:
      if age > homenVelho:
        homenVelho = age
        nameOld = name
  if sex == "F" and age < 20:
    ageMulher += 1
    if sex == "F":
      mulheres += 1
mediaIdade = somaIdade / 4
print(f"A medía de idade do grupo é de {mediaIdade} anos")
print(f"O homen mais velho tem {homenVelho} anos e se chama {nameOld}")
print(f"Ao todos são {mulheres} mulheres ao todo e {ageMulher} mulheres são menos de 20 anos")