t = (int(input("Digite um número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")),
     int(input("Digite o último número: ")))

print(f"você digitou os valores {t}")
print(f"o valor 9 apareceu {t.count(9)} vezes")
if 3 in t:
  print(f"Os valore 3 apareceu na {t.index(3)}° posição")
else:
  print("valor errado...")
print("Os valores pares digitados foram")
for n in t: #pecorre a list uma valor por vez
  if n % 2==0:
    print(n)