times = ("Flamengo","Santos","Palmeiras","Gremio",
         "Atletico Paranaense", "São Paulo","Internacional",
         "Conrithians","Fortaleza","Goias","Bahia","Vasco",
         "Atletico Mineiro","Fluminense","Botafogo","Ceará",
         "Cruzeiro","CSA","Chapecoense","Avaí")

print(times)
print("-"*50)
print(f"os 5 primeiros times são {times[0:5]}")
print("-"*50)
print(f"os últimos 4 colocados {times[-4:]}")
print("-"*50)
print(f"OS TIMES EM ORDEM ALFABETICA {sorted(times)}")
print("-"*50)

print(f"Chapecoense esta na {times.index('Chapecoense')+1}° posição")