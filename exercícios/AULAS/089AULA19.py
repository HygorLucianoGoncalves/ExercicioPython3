pessoas = {"nome": "Ana", "sexo": "F", "idade": 22}

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())
#enserindo mais informção:
pessoas['peso'] = 98.5
print('-' * 30)
for k, v in pessoas.items():
  print(f"{k} {v}")
####################################0
brasil = []
estados1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estados2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estados1)
brasil.append(estados2)

print(brasil)
print(brasil[1])
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
############################

estado = {}
brasil = []
for c in range(0, 3):
  estado['uf'] = str(input("Unidade Federativa: "))
  estado['sigla'] = str(input("Sigla do Estado: "))
  brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
    print(f"o campo {k} tem valor {k}")
