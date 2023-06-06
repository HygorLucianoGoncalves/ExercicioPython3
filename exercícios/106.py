c = ('\033[m','\033[0;30;41m','\033[0;30;42m','\033[0;30;43m','\033[0;30;44m','\033[0;30;45m','\033[0;30m');



def ajuda(com):
  titulo(f"Acessando o manueal do comando \'{com}\'", 4)
  print(c[5], end="")
  help(com)
  print(c[0], end="")
  

def titulo(le, cor=0):
  tam = len(le) + 6
  print(c[cor], end='')
  print("~" * tam) 
  print(f"  {le}")
  print("~" * tam)
  print(c[0], end='')

#principal
msg = " "
while True:
  titulo("SISTEMA DE AJUDA pyHELP",3)
  msg = str(input("Função ou Biblioteca > "))
  if msg.lower() == "fim":
    break
  else:
    ajuda(msg)
titulo("Até logo!",1)