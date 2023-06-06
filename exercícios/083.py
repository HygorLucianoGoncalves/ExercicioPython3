expr = str(input("Digite a expressão: "))
pilha = list()
for i in expr:  #pecorre a expressão de expr
  if i == "(":  #ser tiver ( na lista
    pilha.append("(")  #add na list pilha
  elif i == ")":
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(")")  #add a list ai a list fica com mais 1 e não cair no if
      break
if len(pilha) == 0:
  print("Sua expressão está válida!")
else:
  print("sua expressão está errada!")



####

expressões = str(input("digite a expressões: "))
lista = []
for i in expressões:
  if i == "(":
    lista.append("(")
  elif i == ")":
    if len(lista) > 0:
      lista.pop()
    else:
      lista.append(")")
      break
if len(lista) == 0:
  print("Sua expressão está válida!")
else:
  print("sua expressão está errada!")
