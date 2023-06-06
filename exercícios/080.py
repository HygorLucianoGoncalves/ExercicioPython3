lista = list()

for i in range(0, 5):
  n = int(input("Digite um valor: "))
  if i == 0:
    lista.insert(5, n)
    print("Adicionado ao final da lista...")
    print('-' * 30)
  if i == 1:
    lista.insert(0, n)
    print("Adicionado na posição 0 da lista")
    print('-' * 30)
  if i == 2:
    lista.insert(1, n)
    print("Adicionado na posição 1 da lista")
    print('-' * 30)
  if i == 3:
    lista.insert(5, n)
    print("Adicionado no final da lista")
    print('-' * 30)
  if i == 4:
    lista.insert(0, n)
    print("Adicionado na posição 0 da lista")
    print('-' * 30)
print(f"Os valores digitados em ordem foram {lista}")
