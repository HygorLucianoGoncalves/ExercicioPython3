def teste(nome="",gols=0):
  print(f"o nome do {nome} fez {gols} gol(s) no campeonato.")

#principal 
n = input("Nome do jogador: ").strip()
g = input("Numero de gols: ")

if len(n) == 0:
    n = "<Desconhecido>"
    
if len(g) == 0 or not g.isnumeric():
    g = 0
else:
    g = int(g)

teste(n,g)