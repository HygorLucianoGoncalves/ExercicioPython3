valor1 = int(input("Primeir valor: "))
valor2 = int(input("Segundo valor: "))
menu = True
while menu == True:
  print(
    "[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa"
  )
  opçao = int(input(">>>>>> Qual sua opção?: "))
  if opçao == 1:
    soma = valor1 + valor2
    print(f"A soma entre {valor1} + {valor2} = {soma}")
  elif opçao == 2:
    multi = valor1 * valor2
    print(f"A multiplicação entre {valor1} * {valor2} = {multi}")
  elif opçao == 3:
    if valor1 > valor2:
      print(f"O maior numero é {valor1}")
    else:
      print(f"O maior numero é{valor2}")
  elif opçao == 4:
    nv = int(input("primeiro Número "))
    nv2 = int(input("segundo Número "))
    valor1 = nv
    valor2 = nv2
  elif opçao == 5:
    print("Finaliznado...")
    menu = False
  else:
    print("Opção invalida...Tente novamente")
  print("=-==" * 20)
