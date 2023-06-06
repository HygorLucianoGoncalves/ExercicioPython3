e = ('')
cont = 1
n = int(input("Quer ver a tabuada de qual valor? "))
while cont != 11:
  if n < 0:
    break
  print(f"{e:>7} {n} x  {cont}  = {cont * n}")
  cont += 1
  if cont == 11:#renecia o programa 
    print("-" * 20)
    n = int(input("Quer ver a tabuada de qual valor? "))
    cont = 1
    print("-" * 20)
print("Programa encerrado...")

#feito na aula

while True:
  n =  int(input("Quer ver a tabuada de qual valor? "))
  print("--" * 30)
  if n < 0:
    break
  for c in range(1, 11):
    print(f"{n} x {c} = {n*c}")
  print("--" * 30)
print("Program encerrado  ")