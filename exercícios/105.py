def notas(*n,sit=False):
  '''
  -> Função para analisar notas e situação de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional,indicando se deve ou não adiciomar a situação
  :return: dicrionário com varias informações sobre a situação da turma.
  '''
  info = dict()
  total = soma = media = 0
  while True:
    total += 1
    #maio e menor
    maior = max(n)
    menor = min(n)
    #add na disct
    info["Total"] = total   #LA EM BAIXO TEM A RELOÇÃO MAIS BONITA 5
    info["Maior"] = maior
    info["menor"] = menor
    if total == len(n):
        break
  #media
  for i in n:
    soma += i
  media = soma / total
  info["media"] = media     
  #situação
  if sit:
    if media < 5.0:
      info["situação"] = "RUIM"
    elif media >= 5.0 and media < 7.0:
      info["situação"] = "RAZOÁVEL"
    else: 
      info["situação"] = "BOA"    
  return info 
    
#programa
a = notas(5.5,2.5,10,6.5, sit=True)
print(a)
b = notas(5.5,2.5,1.5, sit=True)
print(b)
c = notas(7.1,8.7,6.1,10, sit=True)
print(c)
help(notas)



#feito no video3

def notas(*n,sit=False):
  '''
  -> Função para analisar notas e situação de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional,indicando se deve ou não adiciomar a situação
  :return: dicrionário com varias informações sobre a situação da turma.
  '''
  info = dict()
  info["Total"] = len(n)
  info["Maior"] = max(n)
  info["menor"] = min(n)
  info["media"] = sum(n)/len(n)
  #situação
  if sit:
    if info["media"] >= 7:
      info["situação"] = "BOA"  
    elif info["media"] >= 5.0:
      info["situação"] = "RAZOÁVEL"
    else: 
      info["situação"] = "RUIM"     
  return info 
    
#programa
a = notas(5.5,2.5,10,6.5, sit=True)
print(a)
b = notas(5.5,2.5,1.5, sit=True)
print(b)
c = notas(7.1,8.7,6.1,10, sit=True)
print(c)


help(notas)
