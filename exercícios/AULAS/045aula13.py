# posso usar de varias formas
n1 = int(input("inicio "))
n2 = int(input("fim "))
n3 = int(input("passo "))

for c in range(n1, n2+1, n3):
  print(c)
print("FIM")

s = 0
for c in range(0, 3):
  n = int(input("Digite un valor"))
  s += n
  print(s)
print(s)
print("FIM")
