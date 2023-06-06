import random
from operator import itemgetter
jogadas = {}
for c in range(1,5):
  jogadas[f"jogador{c}"] = random.randint(0,6)
for i,k in jogadas.items():
  print(f"{i} tirou {k} no dado ")
ranking = sorted(jogadas.items(), key=itemgetter(1),reverse=True)#cmd vai usar mais pra frente#o resuldador sari em list
print("-"*30)
for i,v in enumerate(ranking):
  print(f"{i+1}° lugar: {v[0]} com {v[1]}.")
