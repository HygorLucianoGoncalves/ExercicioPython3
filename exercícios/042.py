a = float(input("primeiro segemento  "))
b = float(input("segundo segmento  "))
c = float(input("terceiro segmento  "))

if a < b + c and b < a + c and c < a + b:
  print("Os segmentos acima não pode fomar um triangulo ", end='')
  if a == b == c:
    print("EQUILÁTERO")
  elif a != b != c != a:
    print("ESCALENO")
  else:
    print("ISOSCELES")
else:
  print("Os segmentos acima não pode forma um triangulo")
