peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))

imc = peso / (altura * altura)  # altura ** 2

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
  print("Abaixo do peso")
elif imc <= 24.9:
  print("Peso normal")
elif imc <= 29.9:
  print("Sobrepeso")
elif imc <= 34.9:
  print("Obesidade grau 1")
elif imc <= 39.9:
  print("Obesidade grau 2")
else:
  print("Obesidade grau 3")
