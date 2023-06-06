a = float(input("primeiro segemento  "))
b = float(input("segundo segmento  "))
c = float(input("terceiro segmento  "))

if (a + b < c) or (a + c < b) or (b + c < a):
  print("Os segmentos acima não pode fomar um triangulo")

else:
  print("Os segmentos acima pode forma um triangulo")0