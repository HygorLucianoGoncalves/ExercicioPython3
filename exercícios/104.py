def testeint(msg):
  global n
  while True:
    print("-"*30)
    n = input((msg))
    if len(n) == 0 or not n.isnumeric():#ser len for 0 ou não for numerico
      print(f"\033[0;31mERRO! Digite um numero inteiro válido.\033[m")
    else:
      n = int(n)
      break
  
#principal
testeint("Digite um numero: ")
print(f"Voce acabou de digitar o número {n}")    