nome = str(input("Digite se nome completo: ")).lower().strip()
separa = nome.split()
print(f"Muito prazer em te conhecer!\nSeu primeiro nome é {separa[0].capitalize()}\nSeu ultimo nome é {separa[-1].capitalize()}\nSeu nome completo e {nome.capitalize()}")