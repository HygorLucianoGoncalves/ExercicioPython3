def cadastrar(arq, nome="<desconhecido>",idade=0):
  try:
    a = open(arq, "at")
  except:
    print("houve um ERRO na abertura do arquivo")
  else:
    try:
      a.write(f"{nome};{idade}\n")
    except:
      print("Houve um ERRO na hora de escrever os dados!")
    else:
      print(f"Novo registro de {nome} adicionado")
      a.close()
      