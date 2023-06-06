r = "S"
soma = cont = media = maior = menor = 0
while r in "Ss":
  n = int(input("Digite um número: "))
  cont += 1
  soma += n
  if cont == 1:  # na primeira contagem pega o primeros valor, ser for maior que os primeiros valor troca la em baixo e se for menor a mesma coisa.
    maior = n  # ou maior = menor = n
    menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
  r = str(input("Quer continuar [S/N] ")).upper().strip()[0]
media = soma / cont
print(f"Você digitou {cont} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
