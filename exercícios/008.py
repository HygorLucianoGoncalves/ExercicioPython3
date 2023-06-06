m = float(input("Uma distancia em metros: "))
dm = m*10
cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dam = m/10

print(f"A medidas são\nQuilômetro {km} km\nHectômetro {hm} hm\nDecâmetro {dam} dam\nDecímetro {dm:.0f} dm  \nCetimetro {cm:.0f} cm \nMilímetro {mm:.0f} mm")
