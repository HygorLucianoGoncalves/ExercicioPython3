#faz o desafio aqui e depois colocar na pasta do munero dos desafio. 000
num = int(input("informe un múmero: "))

unidades = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(
  f"\nAnalisando o número {num}\n\nA unidades: {unidades}\nA dezena: {dezena}\nA centena: {centena}\nO milhar: {milhar}"
)
