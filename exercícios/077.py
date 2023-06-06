vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viajar', 'Elegante', 'Animal', 
            'Carro', 'Brasileiro', 'Abacate')

for i in palavras:#vai pegore a lista e mostra uma palavra de cada vez
  print(f"\nNa palavra {i} temos:  ", end="")
  for l in i:#vai pegore as palavras
    if l.lower() in vogais:#vai verifica ser tem vogais na palavra
      print(l, end=" ")#mostra as vogais encotradas