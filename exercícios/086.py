list = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
 for c in range(0,3):
   list[l] [c] = int(input(f"Digite {c}° valor para [{l}, {c}]: "))
print('-'*30)
for l in range(0,3):
  for c in range(0, 3):
    print(f"[{list[l][c]:^5}]", end=" ")
  print()




matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
  for l in range(0,3):
    matriz[i][l] = int(input(f"Digite um valor para [{i}, {l}]: "))
for i in range(0,3):
  for l in range(0,3):
    print(f"[{matriz[i][l]:^5}]",end="")
  print()