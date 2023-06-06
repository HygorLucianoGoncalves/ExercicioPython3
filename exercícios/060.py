n = int(input("Digite um número para\nCalcular seu Fatorial: "))

resultado = 1
contador = 1

while contador <= n:
  resultado *= contador
  contador += 1
  print(f"{contador} x {n}", end="")
print(f"O cálculo do fatorial é {resultado} ")

#usando import tem no modulo math
#feiro na aula
n = int(input("Digite um número para\nCalcular seu Fatorial: "))
c = n
f = 1
while c > 0:
  print(f"{c}", end="")
  print(" x " if c > 1 else
        " = ", end="")
  f *= c
  c -= 1
print(f)
