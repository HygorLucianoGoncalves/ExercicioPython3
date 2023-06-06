palavra = str(input("Digite uma frase: ")).upper().replace(" ", "")

inverso = palavra[::-1].upper().replace(" ", "")

print(f"O inverso de {palavra} é {inverso}")

if palavra == inverso:
  print("Temos uma palavra Palíndromo")
else:
  print("não temos uma palavra palíndromo")