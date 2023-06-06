def fac(v, show=False):
  r = cont = 1
  while cont <= v:
    if show:
      print(cont,end='')
      if cont < v:
        print(' x ',end='')
      if cont == v:
        print(' = ',end='')
    r *= cont
    cont+=1
    
  return r
print(fac(5,show=True))
print(fac(5))

