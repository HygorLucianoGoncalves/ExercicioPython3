def soma(a, b):
  s = a + b
  print(s)


soma(5, 6)


###########################
def media(nota1, nota2, c):
  media = (nota1 + nota2) / c
  print(f"A media do aluno é = {media}")


media(int(input("Primeira nota do aluno: ")), int(input("Segunda nota: : ")),
      int(input("quantas notas digitada ")))


####################################
def contador(*num):
  tam = len(num)
  print(f"Recebi os valores {num} e são ao todo {tam} números")


contador(2, 2)
contador(2, 2, 5, 6, 365, 8, 9, 1, 4)
contador(4)
contador(
  2,
  2,
  5,
  6,
  365,
  8,
  9,
  1,
  4,
  2,
  2,
  5,
  6,
  365,
  8,
  9,
  1,
  4,
)


#################
def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos] *= 2
    pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
