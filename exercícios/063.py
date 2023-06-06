
quantosTemos = int(input("Quantos temos voçê que ver? "))

valor0 = 0
valor1 = 1

print(f"{valor0} => {valor1}", end=" ")
contagemDeTermos = 3

while contagemDeTermos <= quantosTemos:
  soma = valor0 + valor1
  valor0 = valor1 #pega o valor de 1
  valor1 = soma #pega o valor da soma 
  contagemDeTermos += 1 
  print(f"=> {soma}",end=" ")
print("fim")









##FEITO NO VIDEO 


n = int(input("Quntos termos você quer mostrar? "))

t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end="")
cont = 3# começa no 3 termo
while cont <= n:
  t3 = t1 + t2
  t1 = t2
  t2 = t3
  cont += 1
  print(f"-> {t3}", end="")
print(" Fim")