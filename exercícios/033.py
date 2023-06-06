n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))
n3 = int(input("Digite o terceiro valor "))

v = [n1, n2, n3]

if max(v) != None:
  print(f"o valor maior {max(v)}")
if min(v) != None:
  print(f"O valor menor {min(v)}")

#resolução feita no video
a = int(input("primeiro valor  "))
b = int(input("segundo valor  "))
c = int(input("terceiro valor  "))
#verificar ser e menor
menor = a
if b < a and b < a:
  menor = b
if c < a and c < b:
  menor = c

#verificar  o maior
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c

print(
  f"O menor valor digitado foi {menor}\nO maior valor digitado foi {maior}")
