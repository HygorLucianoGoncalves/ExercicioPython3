sexo  = str(input("informe seu sexo: [M/F]")).strip()

while sexo not in "MmFf":
  sexo  = str(input("Valor errado... informe seu sexo: [M/F]")).strip()[0]
print(f"seu {sexo} resgistrado com sucesso")
  