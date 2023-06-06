i = ("Lápis", 1.75,
     "Borracha", 2.00,
     "Caderno", 15.90, 
     "Estojo", 25.00, 
     "Transferidor", 4.20,
     "Compasso", 9.99, 
     "Mochila", 120.32,
     "Canetas", 22.30, 
     "Livro", 34.90)
print('-'*30)
print(f"listagem de preço: ")
print('-'*30)
for pos in range(0, len(i)): #para cada item #range começa 0 e vai ate o tamanho da list em len
  if pos % 2 == 0:
    print(f"{i[pos]:.<30}", end="")#.<30 colocar 30 pontos os ponto 
  else:
    print(f"R${i[pos]:>10.2f}")