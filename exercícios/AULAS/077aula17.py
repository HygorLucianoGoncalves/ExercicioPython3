#list
num = [2, 5, 9, 1]
num[2] = 3

num.append(7)

num.sort()

num.insert(2, 0)

num.remove(2)
#if 2 in num:
#num.remove(2)
#else:
#print("não achei o numerp 2")

num.pop(2)

print(num)

print(f"essa lista tem {len(num)} elementos")




valores = list()

for i in range(0,5):
  valores.append(int(input("Digite um valor ")))
for contado, valor in enumerate(valores):
  print(f"Na posição {contado} encontrei o valor {valor}!")
print("cheguei ao final da lista")


#copia de list

a = [2,3,4,6]
b = a[:]

b[2] = 8

print(a)
print(b)