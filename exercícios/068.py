import random

tentativas = vitorias = derrotas = 0

while True:
  sorteio = random.randint(0, 10)

  n = int(input("Digite um numero "))

  opção = str(input(
    "PAR ou Impar? [DIGITE SAIR PARA ENCERRAR] [P/I] ")).strip().upper()[0]

  soma = n + sorteio
  if opção == "S":
    break
  elif opção == "P":
    joagador = "PAR"
    computador = "IMPAR"
    print("\nVocê e PAR")
    if soma % 2 == 0:
      resl = "DEU PAR >>> Jogador venceu"
      vitorias += 1
    else:
      resl = "DEU IMPAR >>> computador venceu"
      derrotas += 1
  else:
    joagador = "IMPAR"
    computador = "PAR"
    print("\nVocê e Impar")
    if soma % 2 == 1:
      resl = "DEU IMPAR >>> jogador venceu"
      vitorias += 1
    else:
      resl = "DEU PAR >>> computador venceu"
      derrotas += 1
  print(
    f"\n\nVocê jogou {n} e o computador jogou {sorteio}... Total deu {soma}\n\n{resl}\n"
  )
  print("-=-" * 20)
  tentativas += 1
print(f"\nVocê jogou {tentativas} e venceu {vitorias} e perdeu {derrotas}")
