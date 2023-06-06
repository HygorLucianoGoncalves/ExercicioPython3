def leiaDinheiro(msg):
  valido = False
  while not valido:
    entrada = str(input(msg)).replace(",",".").strip()
    if entrada.isalpha() or entrada == "":
      print(f"\033[0;31mERRO! Digite um numero válido.\033[m") 
    else:
      valido = True
      return float(entrada)
      