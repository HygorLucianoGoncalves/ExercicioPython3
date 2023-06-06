n = 1
cont = -1
soma = 0
while n != 0:
  if n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    cont += 1
  if n == 999:
    n = 0
  soma += n
print(f"Você digitoi {cont} números e a soma entre eles foi {soma}")

#feita na aula

num = cont = soma = 0

num = int(input("Digite um número [999 para parar]: "))

while num != 999:
  soma += num
  cont += 1
  num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitoi {cont} números e a soma entre eles foi {soma}")
