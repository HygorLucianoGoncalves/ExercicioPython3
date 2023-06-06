def aumentar(preço, taxa, estilo=False):
  res = preço + (preço * taxa / 100)
  return res if estilo is False else moeda(res)


def diminuir(preço, taxa, estilo=False):
  res = preço - (preço * taxa / 100)
  return res if estilo is False else moeda(res)


def dobro(preço, estilo=False):
  res = preço * 2
  return res if estilo is False else moeda(res)


def metade(preço, estilo=False):
  res = preço / 2
  return res if estilo is False else moeda(res)


def moeda(preço=0, moeda="R$"):
  return f"{moeda}{preço:.2f}".replace(".",
                                       ",")  #replace troca o . e colocar ,


def resumo(preço=0, taxaum=0, taxadim=0):
  print("-" * 30)
  print("RESUMO DO VALOR".center(30))
  print("-" * 30)
  print(f"Preço analisado: \t{moeda(preço)}")
  print(f"Dobro do preço: \t{dobro(preço,True)}")
  print(f"Metade do preço: \t{metade(preço,True)}")
  print(f"{taxaum}% de aumento: \t{aumentar(preço,taxaum,True)}")
  print(f"{taxadim}% de redução: \t{diminuir(preço,taxadim,True)}")
  print("-" * 30)
