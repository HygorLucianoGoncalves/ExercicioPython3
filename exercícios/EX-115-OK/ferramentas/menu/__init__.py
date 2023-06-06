def leiaInt(msg):#ler so  numero inteiro
  while True:
    try:
      n = int(input(msg))
    except:
      print(f"\033[0;31mERRO! Digite um numero válido.\033[m")
      continue
    else:
      return n


def cabeçalho(txt):#estilo de cabeçalho
  print()
  print("-" * 50)
  print(txt.center(50))
  print("-" * 50)


#menu que vai aparecer menu pricipal
def menu(lista):
  cabeçalho("MENU PRINCIPAL")
  c = 1
  for item in lista:#cria uma cabeçalho automatico
    print(f"{c} - {item}")
    c += 1
  print("-" * 50)
  opc = leiaInt("Sua Opção: ")
  return opc

    
  