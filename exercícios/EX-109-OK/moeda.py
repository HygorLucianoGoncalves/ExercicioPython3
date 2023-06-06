def aumentar(preço, taxa, estilo=False):
  res = preço + (preço * taxa / 100)
  return res if estilo is False else moeda(res)


def diminuir(preço, taxa, estilo=False):
  res = preço - (preço * taxa / 100)
  return res if estilo is False else moeda(res)


def dobro(preço,estilo=False):
  res = preço * 2
  return res if estilo is False else moeda(res)


def metade(preço,estilo=False):
  res = preço / 2
  return res if estilo is False else moeda(res)


def moeda(preço=0, moeda="R$"):
  return f"{moeda}{preço:.2f}".replace(".",",")  #replace troca o . e colocar ,
  
