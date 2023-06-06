import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

list = [a1, a2, a3, a4]
sorteio = random.choice(list)

print(f"\nO aluno sorteiado foi o {sorteio}")
