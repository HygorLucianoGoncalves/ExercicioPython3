nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao total {len(nome)-nome.count(' ')} letras")
separa = nome.split()
print(f"Seu primeiro nome e {separa[0]} e ele tem {len(separa[0])} letras")

print("\n")

print(
  f"Analisando seu nome...\nSeu nome em maiúscilas e {nome.upper()}\nSeu nome em minúsculas é {nome.lower()}\nSeu nome tem  ao total {len(nome)-nome.count(' ')}\nSeu primeiro nome e {separa[0]} e ele tem {len(separa[0])} "
)
