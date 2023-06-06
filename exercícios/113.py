def inteiro(msg):
  while True:
    try:
      n = int(input(msg))
    except:
      print(f"\033[0;31mERRO! Digite um numero válido.\033[m") 
      continue
    else:
      return n

def real(msg):
  while True:
    try:
      a = float(input(msg))
    except:
      print(f"\033[0;31mERRO! Digite um numero válido.\033[m") 
      continue
    else:
      return a
  
  
N = inteiro("Digite um Inteiro: ")
A = real("Digite um Real: ")
print(f"O valor inteiro digitado foi {N} e o real foi {A} ")