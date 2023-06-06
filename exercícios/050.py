soma = 0  #variavel que faz a soma
contagem = 0  #variavel que faz a contagem de numeros digitado funciona como um contagem++
for i in range(1, 7):  #vai mostra a varial n 6 vezes
  n = int(input(f"Digite o {i} valor: "))
  if n % 2 == 0:  #se o numero digitado tiver o resto da divisão em 2 % == 0, sigifica que e par, então a soma e a contgem acontecer
    soma += n
    contagem += 1
print(f"voce informou {contagem} numeros e a soma foi {soma}")

soma = 0
contagem = 0
for i in range(1, 7):
  numero = int(input(f"Digite um {i} valor : "))
  if numero % 2 == 0:
    soma += numero
    contagem += 1

print(f"voce informou {contagem} numeros e a soma foi {soma}")
