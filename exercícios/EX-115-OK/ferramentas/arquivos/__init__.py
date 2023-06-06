from ferramentas.menu import *

def aquivoExiste(nome):
  try:
    a = open(nome,"rt")
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
    

def criaArquivo(nome):
  try:
    a = open(nome, "xt+")
    a.close()
  except:
    print("Houve um erro na criação do arquivo!")
  else:
    print(f"Arquivo {nome} criado com sucesso!")

def lerArquivo(nome):
  try:
    a = open(nome, 'rt')
  except:
    print("Erro ao ler o arquivo!")
  else:
    cabeçalho("PESSOAS CADASTRADAS")
    for linha in a:
      dado = linha.split(';')
      dado[1] = dado[1].replace("\n", '')
      print(f"{dado[0]:<30}{dado[1]:>3} anos")
  finally:
    a.close()
    



