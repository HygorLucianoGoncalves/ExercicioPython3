dis = float(input("Qual a distância da viagem? : "))

if dis <= 200:
  print(f"o valor da viagem e R${dis * 0.50:.2f}")
else:
  print(f"O valor da viagem e R${dis * 0.45:.2f}")