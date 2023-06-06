#tuplas
lanche = ("maça","banana","abacaxi","laranja")
# Tupas são imutáveis
print(lanche[3])
print(lanche[1:2])
print(lanche[:2])
print(lanche[-3])
print(lanche)
print(len(lanche))
print(sorted(lanche))

print("--"*30)

for i in lanche:
  print(f"eu vou lancha {i} ")
  
print("--"*30)

for x in range(0, len(lanche)):
  print(f"eu vou comer {lanche[x]},na posição {x}")
  
print("--"*30)

for pos, comida in enumerate(lanche):
  print(f"Eu vou comer {comida} na posição {pos}")
  
print("--"*30)

a = (2, 5, 4)
b = (5, 8 ,1 ,2)
c = a + b
print(c)
print(c.count(4))#Quantas vez aparece
print(c.index(8))

del(lanche)#apaga a tupla

print("--"*30)


