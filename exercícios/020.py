import random

n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

list = [n1, n2, n3, n4]

random.shuffle(list)

print(f"A ordem de aluno são {list}")
