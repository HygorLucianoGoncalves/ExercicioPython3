import datetime

dataAtual = datetime.date.today().year
def voto(ano):
  s = dataAtual - ano
  if s < 16:
    return f"Com {s} anos: NÃO VOTA"
  elif 16 <= s < 18 or s > 65:
    return f"Com {s} anos: VOTO OPCIONAL."
  else: 
    return f"Com {s} anos: VOTO OBRIGATORIO."
  
a = int(input("Em que ano você nasceu? "))
print(voto(a))