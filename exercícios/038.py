v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

v = [v1, v2]

if v1 == v2:
  print("valores igual")
elif v != None:
  print(f"O valor maximo e {max(v)}\nO valor menor e {min(v)}")
else:
  print("Valor invalido")

#resolução feira na aula 

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
  print("O primeiro valor a maior. ")
elif n2 > n1:
  print("O segundo valor e maior.")
else: 
  print("O valores são igual")