dados = dict()
jogadores = list()
while True: 
  dados["nome"] = str(input("Nome do jogador: ")).strip()
  dados["qParti"] = int(input(f"Quntas partidas {dados['nome']} jogou? "))
  dados["gol"] = list()  
  for i in range(1, dados["qParti"]+1):
    dados["gol"].append(int(input(f"    Quantos gols na partida {i}? ")))
  dados["total"] = sum(dados["gol"])
  jogadores.append(dados.copy())

  r = " "
  while r not in "NnSs":
    r = str(input("Quer continuar? [S/N] ")).strip()
  if r in "Nn":
    print("-="*30)
    break
print(f"{'COD'}{'nome':>10}{'gols':>15}{'total':>30}")
print("--"*30)
for c, i in enumerate(jogadores):
  print(f"{c}{i['nome']:>10}{i['gol']!s:>15}{i['total']:>30}")
  print()
print("--"*30)
while True:
  opção = int((input("Mostra dados de qual jodadores? (999 para parar) ")))
  if opção == 999:
    break
  if opção >= len(jogadores):
    print(f"ERRO! jogado de numero {opção} não existe")
  else:
    print(f"-- LEVANTMENTO DO JOGADOR {jogadores[opção]['nome']}:")
    for c, i in enumerate(jogadores[opção]["gol"]):
      print(f"    No jogo {c+1} fez {i}  gols")
    print("--"*30)
  
