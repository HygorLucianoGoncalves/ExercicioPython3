n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = " "

while True:
  i = int(input("Digite um numero entre 0 e 20: "))
  if 0 <= i <= 20:
    print(f"Voçe digitou o numero {n[i].upper()}")
  else:
    print("Valor errado...")
  cont = " "
  while cont not in "SN":
    cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("--"*20)
  if cont == "N":
    break
print(f"{'-'*20} FIM DO PROGRAMA {'-'*20}")
   
  
