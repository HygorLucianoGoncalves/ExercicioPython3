valores = list()


while True:
  n = int(input("Digite um valor "))
  if n not in valores:#ser n não estiver em valores adicionar ser não so print na dela
    valores.append(n)
    print("valor adicionado com sucesso...")
  else:
    print("Valor duplicado...Não adicionado")  
  # 
  r = " "
  while r not in "SN":
    r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("-"*30)
  if r == "N":
    break
#list em ordem 
valores.sort()
#  
print(f"{valores}")