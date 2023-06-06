jogo = dict()

jogo["nome"] = str(input("Nome do Jogador "))
qParti = int(input(f"Quantas partidas {jogo['nome']} jogou?  "))
jogo["gols"] = []
for i in range(0, qParti):
  jogo["gols"].append(int(input(f"Quantos gols na partida {i}? " )))
jogo["total"] = sum(jogo["gols"])
print("-="*30)
print(jogo)
print("-="*30)
for k, v in jogo.items():
  print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jogo['nome']} jogou {qParti} partidas.") 
for i in range(0,qParti):#oe podia fazer com enumerate pq e uma lista o que esta dentro de gols 
  print(f"    => Na partida {i}, fez {jogo['gols'][i]} gols.")
print(f"Foi um total de {jogo['total']} gols.")  