def maior(*lst):
  maior = 0
  print("Analisando os valores passados...")
  for i in lst:
    print(i, end=" ")
    if i > maior:
      maior = i
  print(
    f"foram informados {len(lst)} valores ao todo.\nO maior valor informado foi {maior}."
  )
  print("_-" * 30)


maior(7, 2, 5, 0, 4)
maior(9, 5, 6, 10, 23)
maior(1)
maior(7, 2, 5, 0, 4, 9, 45, 65)
