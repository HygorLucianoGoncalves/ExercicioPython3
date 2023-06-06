km = int(input("Quandos km você rodou com o carro? "))
dias = int(input("Quandos dias você ficou com o carro? "))

cal = km * 0.15
cal2 = dias * 60
total = cal + cal2

print(f"O valor total foi de {total} R$")

#podemos fazer sem var 

print(f"O valor total foi de {(km*0.15) + (dias*60)} R$")