n = int(input("Digite um número: "))
con = 0
for i in range(1, n + 1):
  if n % i == 0:
    print(f'O numero {n} é divisível por {i}.')
    con += 1
if con == 2:
  print("Esee numero e primo")
else:
  print("Esse valor não e primo")

print(f"\nO numero {n} foi divisivel {con} vezes")








##feito no video

num = int(input("Digite um número: "))
contagem = 0
for c in range(1, n + 1):
  if num % c == 0:
    print("\033[32m")
    contagem += 1
  else:
    print("\033[31m")
  print(c)
print(f"\n\033[32mO número {num} foi divisivel {contagem} vezes")
